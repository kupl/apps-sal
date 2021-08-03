from collections import Counter


class Solution:
    def canReorderDoubled(self, A: List[int]) -> bool:
        if len(A) % 2 == 1:
            return False
        if not A:
            return True
        nums = sorted(set(A))
        nums = [x for x in nums if x < 0][::-1] + [x for x in nums if x >= 0]
        c = Counter(A)
        done = set()
        for num in nums:
            if num in done:
                continue
            if 2 * num not in c:
                return False
            if c[2 * num] < c[num]:
                return False

            c[2 * num] -= c[num]
            if c[2 * num] == 0:
                done.add(2 * num)

            c[num] = 0
            done.add(num)

        return True
