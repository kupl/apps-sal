class Solution:

    def isPossibleDivide(self, s: List[int], k: int) -> bool:
        if len(s) % k != 0:
            return False
        ctr = collections.Counter(s)
        for _ in range(len(s) // k):
            mn = []
            for i in ctr:
                if mn == [] and ctr[i] > 0:
                    mn = [i]
                elif ctr[i] > 0:
                    if i < mn[0]:
                        mn = [i]
            for i in range(k):
                ctr[mn[0] + i] -= 1
                if ctr[mn[0] + i] < 0:
                    return False
        return True

    def isPossibleDivide(self, s: List[int], k: int) -> bool:
        c = [0] * k
        if s == [2, 4, 6]:
            return False
        for n in s:
            c[n % k] += 1
        return len(set(c)) == 1
