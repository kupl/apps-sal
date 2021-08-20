class Solution:

    def canReorderDoubled(self, A: List[int]) -> bool:
        cnt = collections.Counter(A)
        for k in sorted(cnt, key=abs):
            if cnt[k] > cnt[2 * k]:
                return False
            cnt[2 * k] -= cnt[k]
        return True
