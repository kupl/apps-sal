from collections import Counter


class Solution:
    def threeSumMulti(self, A: List[int], target: int) -> int:
        c = Counter(A)
        res = 0
        s = list(set(A))
        s.sort()
        trips = set()
        for i in range(len(s)):
            if i > target / 3:
                break
            n = s[i]
            l = i
            r = len(s) - 1
            while l <= r:
                a = s[i] + s[l] + s[r]
                if a == target:
                    trips.add((s[i], s[l], s[r]))
                    l += 1
                    r -= 1
                elif a > target:
                    r -= 1
                else:
                    l += 1
        print(trips)
        for t in trips:
            a = 1
            for n in set(t):
                count = c[n]
                if t.count(n) == 3:
                    a *= count * (count - 1) * (count - 2) / 6
                elif t.count(n) == 2:
                    a *= count * (count - 1) / 2
                else:
                    a *= count
            res += a
        return int(res) % (10**9 + 7)
