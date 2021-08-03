class Solution:
    def minDays(self, n: int) -> int:
        ans = 0
        q1, q2 = [n], []
        seen = set()
        while q1:
            for u in q1:
                if u == 0:
                    return ans
                seen.add(u)
                if u % 2 == 0 and u // 2 not in seen:
                    q2.append(u // 2)
                if u % 3 == 0 and u // 3 not in seen:
                    q2.append(u // 3)
                if u - 1 not in seen:
                    q2.append(u - 1)
            q1, q2 = q2, []
            ans += 1
        return ans
