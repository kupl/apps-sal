class Solution:

    def canArrange(self, arr: List[int], k: int) -> bool:
        cnt = [0] * k
        for a in arr:
            a %= k
            remainder = (k - a) % k
            if cnt[remainder] > 0:
                cnt[remainder] -= 1
            else:
                cnt[a] += 1
        return all((c == 0 for c in cnt))
