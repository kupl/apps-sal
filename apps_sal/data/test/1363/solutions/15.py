import math
from bisect import bisect_right as bis


def nCr(n, r):
    if r > n:
        return 0
    f = math.factorial
    return f(n) // f(r) // f(n - r)


g, d, f = list(map(int, input().split()))

gs = list(map(int, input().split()))
gs.sort()
ds = list(map(int, input().split()))
ds.sort()
fs = list(map(int, input().split()))
fs.sort()


def find_max(first, nums):
    nums_max = 0
    for i in range(bis(nums, first), len(nums)):
        if nums[i] <= first * 2:
            nums_max += 1
        else:
            break
    return nums_max


def count_by_first(first, gs_count=1, ds_count=2, fs_count=3):
    gs_max = find_max(first, gs)
    ds_max = find_max(first, ds)
    fs_max = find_max(first, fs)
    return nCr(gs_max, gs_count) * nCr(ds_max, ds_count) * nCr(fs_max, fs_count)


answer = 0
for i in gs:
    answer += count_by_first(i, gs_count=0)
for i in ds:
    answer += count_by_first(i, ds_count=1)
for i in fs:
    answer += count_by_first(i, fs_count=2)

print(answer)
