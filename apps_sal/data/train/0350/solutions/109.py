from collections import Counter


def subarraysWithAtMostK(arr: list, k: int) -> int:
    start = 0
    counter = Counter()
    res = 0

    for end in range(len(arr)):
        num = arr[end]
        counter[num] += 1

        # more than k distinct numbers
        # need to shrink
        while len(counter) > k:
            to_remove = arr[start]
            counter[to_remove] -= 1
            if counter[to_remove] == 0:  # remove if frequency reduces to zero
                del counter[to_remove]
            start += 1

        res += end - start + 1

    return res


def subarraysWithKDistinct(arr: list, k: int) -> int:
    # exactly k => atmost(k) - atmost(k - 1)
    return subarraysWithAtMostK(arr, k) - subarraysWithAtMostK(arr,  k - 1)

class Solution:
    def subarraysWithKDistinct(self, A: List[int], K: int) -> int:
        return subarraysWithKDistinct(A, K)

