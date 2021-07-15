class Solution:
    def minDays(self, n: int) -> int:
        q = [n]
        days = 1
        seen = set()
        while q:
            new_q = []
            for each in q:
                if each == 1:
                    return days
                seen.add(each)
                if each % 2 == 0 and each // 2 not in seen:
                    new_q.append(each // 2)
                if each % 3 == 0 and each // 3 not in seen:
                    new_q.append(each // 3)
                if each - 1 not in seen:
                    new_q.append(each - 1)
            q = new_q
            days += 1
