# 1567. Maximum Length of Subarray With Positive Product

def sgn(n):
    if n > 0:
        return +1
    elif n < 0:
        return -1
    else:
        return 0


def split_0(arr):
    arr_buffer = []
    for elem in arr:
        if elem != 0:
            arr_buffer.append(elem)
        else:
            yield arr_buffer
            arr_buffer = []
    assert len(arr_buffer) == 0


def partial_products(arr):
    prod = 1
    yield prod
    for elem in arr:
        prod *= elem
        yield prod


def get_subarr_max_len(arr):
    # zero-free
    first_index = {}
    max_len = 0
    for (i, prod) in enumerate(partial_products(arr)):
        first_index.setdefault(prod, i)
        max_len = max(max_len, i - first_index[prod])
    return max_len


def get_max_len(arr):
    arr = [sgn(x) for x in arr]
    arr.append(0)

    if len(arr) == 0:
        return 0

    return max(get_subarr_max_len(subarr) for subarr in split_0(arr))


class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        return get_max_len(nums)
