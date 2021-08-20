import math


def cmp(a):
    return a[0] - a[1]


n = int(input())
res = 0
arr = []
for i in range(n):
    (a, b) = list(map(int, input().split()))
    arr.append((a, b))
arr.sort(key=cmp, reverse=True)
for i in range(len(arr)):
    res += arr[i][0] * i + arr[i][1] * (n - i - 1)
print(res)
