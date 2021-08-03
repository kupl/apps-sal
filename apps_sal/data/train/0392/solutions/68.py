from functools import reduce, lru_cache


class Solution:
    def numWays(self, arr: str) -> int:
        arr = list(arr)
        count = reduce((lambda accu, element: accu
                        + (1 if element == '1' else 0)), arr, 0)
        if count % 3 != 0:
            return 0
        if count == 0:
            return ((len(arr) - 1) * (len(arr) - 2) >> 1) % (10**9 + 7)

        target = count / 3

        accu = 0
        ways_of_first_cut = 0
        ways_of_second_cut = 0
        for c in arr:
            if c == '1':
                accu += 1
            if accu == target:
                ways_of_first_cut += 1
            elif accu == target * 2:
                ways_of_second_cut += 1

        return (ways_of_first_cut * ways_of_second_cut) % (10**9 + 7)
