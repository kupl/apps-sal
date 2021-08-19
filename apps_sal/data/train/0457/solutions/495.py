class Solution:

    def coinChange(self, coins: List[int], amount: int) -> int:
        if not amount:
            return 0
        q = deque([amount])
        hs = [False] * amount
        count = 0
        while q:
            l = len(q)
            while l:
                n = q.popleft()
                for c in coins:
                    x = n - c
                    if not x:
                        return count + 1
                    if x > 0 and (not hs[x]):
                        hs[x] = True
                        q.append(x)
                l -= 1
            count += 1
        return -1
