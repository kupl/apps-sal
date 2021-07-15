from typing import List


def get_max(arr: List[int]) -> int:

    mx_running = mx_total = 0

    for n in arr:
        mx_running = n + max(0, mx_running)
        mx_total = max(mx_total, mx_running)

    return mx_total


def get_repeated_max(arr: List[int],
                     k: int,
                     p: int) -> int:

    mx_1 = get_max(arr)
    if k == 1:
        return mx_1 % p
    else:
        mx_2 = get_max(arr + arr)
        if mx_1 > mx_2:
            return mx_1 % p
        else:
            return mx_2 + max(sum(arr) * (k - 2), 0) % p


class Solution:
    def kConcatenationMaxSum(self, arr: List[int], k: int) -> int:
        return get_repeated_max(arr, k, int(1e9 + 7))

