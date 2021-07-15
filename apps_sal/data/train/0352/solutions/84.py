class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        auxList = [(len(item), item) for item in set(words)]
        auxList.sort()
        auxCntList = [1] * len(auxList)
        ans = 1

        for idx, (wordLen, word) in enumerate(auxList):
            for jdx in range(idx+1, len(auxList)):
                cWordLen, cWord = auxList[jdx]
                if cWordLen > wordLen + 1:
                    break
                elif cWordLen == wordLen:
                    pass
                else:
                    for pivot in range(len(cWord)):
                        if cWord[:pivot] + cWord[pivot+1:] == word:
                            auxCntList[jdx] = auxCntList[idx] + 1
                            ans = max(ans, auxCntList[jdx])

        return ans

