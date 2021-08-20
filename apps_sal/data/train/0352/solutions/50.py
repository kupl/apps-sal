class Solution:

    def plusOne(self, a, b):
        bigger = max([a, b], key=len)
        smaller = min([a, b], key=len)
        for i in range(len(bigger)):
            if bigger[:i] + bigger[i + 1:] == smaller:
                return True
        return False

    def longestStrChain(self, words: List[str]) -> int:
        memo = {}
        sort = [[i for i in words if len(i) == a] for a in set([len(j) for j in words])][::-1]
        print(sort)
        for (i, row) in enumerate(sort):
            if i == 0:
                for j in row:
                    memo[j] = 1
            else:
                for a in row:
                    values = []
                    for b in sort[i - 1]:
                        if self.plusOne(a, b):
                            print((a, b))
                            values.append(1 + memo[b])
                    memo[a] = max(values) if values else 1
        return max(memo.values())
