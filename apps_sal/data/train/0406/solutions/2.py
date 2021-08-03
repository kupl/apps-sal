class Solution():
    def ladderLength(self, beginWord, endWord, wordDict):
        front, back = set([beginWord]), set([endWord])
        wordDict = set(wordDict)
        length = 2
        width = len(beginWord)
        charSet = 'abcdefghijklmnopqrstuvwxyz'

        if endWord not in wordDict:
            return 0

        while front:
            newFront = set()

            for phase in front:
                for i in range(width):
                    for c in charSet:
                        nw = phase[:i] + c + phase[i + 1:]
                        if nw in back:
                            return length
                        if nw in wordDict:
                            newFront.add(nw)
            front = newFront

            if len(front) > len(back):
                front, back = back, front

            wordDict -= wordDict & front
            length += 1

        return 0
