from collections import defaultdict


class Solution:
    def canReorderDoubled(self, A: List[int]) -> bool:

        A.sort()

        arr = defaultdict(int)

        for item in A:

            if 2 * item in arr and arr[2 * item] > 0:
                arr[2 * item] -= 1
            elif item % 2 == 0 and (item // 2) in arr and arr[item // 2] > 0:
                arr[item // 2] -= 1
            else:
                arr[item] += 1

        return sum([x for x in arr.values() if x != 0]) == 0
