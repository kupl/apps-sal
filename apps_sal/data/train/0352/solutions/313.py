class Solution:
    def checkPre(self, small, large):

        i = 0
        j = -1

        while True:
            l = r = True
            if i < len(small) and small[i] == large[i]:
                i += 1
            else:
                l = False

            if j + len(small) >= 0 and small[j] == large[j]:
                j -= 1
            else:
                r = False

            if not l and not r:
                break

        return i - j >= len(large)

    def longestStrChain(self, words: List[str]) -> int:
        table = dict()
        small = 10000
        large = 0

        for i in range(len(words)):
            length = len(words[i])
            if length not in table:
                small = min(length, small)
                large = max(length, large)
                table[length] = [i]
            else:
                table[length].append(i)

        pre = [1 for i in range(len(words))]
        for i in range(small, large):
            for j in range(len(table[i])):
                for k in range(len(table[i + 1])):
                    if self.checkPre(words[table[i][j]], words[table[i + 1][k]]):
                        pre[table[i + 1][k]] = max(pre[table[i + 1][k]], pre[table[i][j]] + 1)

        return max(pre)
