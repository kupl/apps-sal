
from collections import Counter


def f(arr):
    cnt = Counter(arr)

    return max(cnt.values())


n = int(input())
arr = [int(i) for i in input().split()]
print(f(arr))
