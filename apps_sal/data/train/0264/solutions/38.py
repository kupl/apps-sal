from itertools import combinations


class Solution:

    def maxLength(self, arr: List[str]) -> int:
        max_count = 0
        for i in range(0, len(arr) + 1):
            comb = combinations(arr, i)
            for c in comb:
                count = 0
                bag = set()
                s = ''.join(c)
                for k in s:
                    if k in bag:
                        count = 0
                        break
                    else:
                        count += 1
                        bag.add(k)
                max_count = max(max_count, count)
        return max_count
