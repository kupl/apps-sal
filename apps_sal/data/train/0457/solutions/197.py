class Solution:

    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        memo = {}

        def helper(target, options):
            if target in memo:
                return memo[target]
            else:
                best = None
                for opt in options:
                    if opt == target:
                        memo[target] = 1
                        return 1
                    elif opt < target:
                        cont = helper(target - opt, options)
                        if cont is not None and (best is None or cont + 1 < best):
                            best = cont + 1
                memo[target] = best
                return best
        output = helper(amount, coins)
        return output if output is not None else -1
