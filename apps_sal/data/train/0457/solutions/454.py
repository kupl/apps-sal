class Solution:
    def coinChange(self, coins: [int], amount: int) -> int:
        self.ans = float('inf')
        self.dict = {}  # amount : [depth]
        coins.sort(reverse=True)

        def helper(num, depth):

            if num == 0:
                self.ans = min(self.ans, depth)
                return

            for c in coins:
                res = num - c
                if res >= 0:
                    if res in self.dict:
                        if self.dict[res] > depth + 1 and depth + 1 < self.ans:
                            self.dict[res] = depth+1
                            helper(res, depth + 1)
                    else:
                        self.dict[res] = depth + 1
                        helper(res, depth + 1)

        helper(amount, 0)
        return self.ans if self.ans < float('inf') else -1

