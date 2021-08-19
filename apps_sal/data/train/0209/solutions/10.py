class Solution:

    def mergeStones(self, stones: List[int], K: int) -> int:
        if (len(stones) - 1) % (K - 1) != 0:
            return -1
        prefix = [0]
        for stone in stones:
            prefix.append(prefix[-1] + stone)
        memo = {}

        def recur(i: int, j: int, m: int):
            key = str(i) + ',' + str(j) + ',' + str(m)
            if key in memo:
                return memo[key]
            if (j - i + 1 - m) % (K - 1):
                return 91111111
            if j - i + 1 < K:
                memo[key] = 0
                return 0
            if m == 1:
                if j - i + 1 == K:
                    memo[key] = prefix[j + 1] - prefix[i]
                    return memo[key]
                else:
                    return recur(i, j, K) + prefix[j + 1] - prefix[i]
            min_sum = 91111111
            for mid in range(i, j, K - 1):
                cur_sum = recur(i, mid, 1) + recur(mid + 1, j, m - 1)
                min_sum = min(min_sum, cur_sum)
            memo[key] = min_sum
            return min_sum
        return recur(0, len(stones) - 1, 1)
