
class Window:
    def __init__(self):
        self.count = {}

    def add(self, elem):
        self.count.setdefault(elem, 0)
        self.count[elem] += 1

    def remove(self, elem):
        self.count[elem] -= 1
        if self.count[elem] == 0:
            del self.count[elem]

    def added_size(self, elem):
        return len(self.count) + bool(elem not in self.count)


def count_below(arr, k):
    if k == 0:
        return 0
    else:
        right = 0
        satisfactory = 0
        window = Window()
        for left in range(len(arr)):
            while right < len(arr) and window.added_size(arr[right]) <= k:
                window.add(arr[right])
                right += 1
            satisfactory += (right - left)
            window.remove(arr[left])
        return satisfactory


def subarrays_with_k_distinct(arr, k):
    assert k >= 1
    return count_below(arr, k) - count_below(arr, k - 1)


class Solution:
    def subarraysWithKDistinct(self, A: List[int], K: int) -> int:
        return subarrays_with_k_distinct(A, K)
