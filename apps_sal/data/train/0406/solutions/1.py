class Solution:
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """

        words = set(wordList)
        if endWord not in words:
            return 0

        beginQ, endQ = {beginWord}, {endWord}
        dist = 2
        while beginQ:
            print(('beginQ', beginQ, 'endQ', endQ))
            newq = set()
            for u in beginQ:
                for i in range(len(u)):
                    for c in 'abcdefghijklmnopqrstuvwxyz':
                        v = u[:i] + c + u[i + 1:]
                        if v in words:
                            if v in endQ:
                                return dist
                            newq.add(v)

            dist += 1
            beginQ = newq
            if len(beginQ) > len(endQ):
                beginQ, endQ = endQ, beginQ

            words -= beginQ

        return 0
