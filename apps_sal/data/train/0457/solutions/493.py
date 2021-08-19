class Solution:

    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        (res, seen, curr) = (0, set(), {c for c in coins if c <= amount})
        while curr:
            res += 1
            if amount in curr:
                return res
            seen |= curr
            tmp = {n + c for n in curr for c in coins}
            curr = {t for t in tmp if t not in seen and t <= amount}
        return -1
