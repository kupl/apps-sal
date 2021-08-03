from collections import defaultdict


class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        # ctr = set([])
        # for i in range(len(arr)):
        #     for j in range(i+1, len(arr)):
        #         if (arr[i] + arr[j]) % k == 0:
        #             if i in ctr or j in ctr:
        #                 continue
        #             else:
        #                 ctr.add(i)
        #                 ctr.add(j)
        # return len(ctr)/2 == len(arr)/2

        if len(arr) % 2 == 1:
            return False
        lookup = defaultdict(int)
        count = 0
        for idx, num in enumerate(arr):
            key = k - (num % k)
            if key in lookup and lookup[key] >= 1:
                count += 1
                lookup[key] -= 1
            else:
                lookup[(num % k) or k] += 1
        return count == len(arr) // 2
