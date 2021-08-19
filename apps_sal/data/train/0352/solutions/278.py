class Solution:

    def longestStrChain(self, words: List[str]) -> int:

        def pred(origin, dest):
            if len(dest) - len(origin) != 1:
                return False
            misWord = False
            oIndex = 0
            for index in range(len(dest)):
                if oIndex == len(origin):
                    if misWord == False:
                        return True
                    return False
                if dest[index] != origin[oIndex]:
                    if misWord:
                        return False
                    misWord = True
                    continue
                oIndex += 1
            return True
        table = {}

        def helper(node):
            longest = 0
            if node in table:
                return table[node]
            for word in words:
                if pred(node, word):
                    longest = max(helper(word), longest)
            table[node] = longest + 1
            return longest + 1
        maxPos = 0
        for word in words:
            maxPos = max(maxPos, helper(word))
        return maxPos
