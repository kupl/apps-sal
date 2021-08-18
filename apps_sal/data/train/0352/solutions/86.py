class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        auxList = [(len(item), item) for item in set(words)]
        auxList.sort()

        auxGraph = collections.defaultdict(set)
        seen = dict()

        for idx, (wordLen, word) in enumerate(auxList):
            seen[word] = False
            for jdx in range(idx + 1, len(auxList)):
                cWordLen, cWord = auxList[jdx]
                if cWordLen > wordLen + 1:
                    break
                elif cWordLen == wordLen:
                    pass
                else:
                    for pivot in range(len(cWord)):
                        if cWord[:pivot] + cWord[pivot + 1:] == word:
                            auxGraph[word].add(cWord)
        ans = 0
        auxDeque = collections.deque()
        for _, word in auxList:
            if seen[word]:
                pass
            else:
                seen[word] = True
                auxDeque.append((1, word))

                while len(auxDeque) > 0:
                    cLen, cnode = auxDeque.pop()
                    ans = max(ans, cLen)
                    for eachNeighbor in auxGraph[cnode]:
                        if not seen[eachNeighbor]:
                            seen[eachNeighbor] = True
                            auxDeque.append((cLen + 1, eachNeighbor))
        return ans
