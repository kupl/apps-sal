import collections


class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        if len(nums) % k != 0:
            return False
        num_of_sets = int(len(nums) / k)
        c = collections.deque([0] * num_of_sets)

        ct = {}
        for n in nums:
            ct[n] = ct.get(n, 0) + 1

        last_num = None
        for num in sorted(ct.keys()):
            if last_num is not None and num != last_num + 1 and any(cc != 0 for cc in c):
                return False

            amount = ct[num]
            for i in range(num_of_sets):
                if amount > 0:
                    c[i] = (c[i] + 1) % k
                    amount -= 1
                elif c[i] != 0:
                    return False

            if amount > 0:
                return False

            i = 0
            while c[0] == 0 and i < num_of_sets:
                c.append(c.popleft())
                i += 1

            last_num = num

        return all(cc == 0 for cc in c)
