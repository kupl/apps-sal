import math
import re


def f(arr, n):
    a = set()
    x = 0
    y = sum(arr)
    res = 'NO'
    for i in range(n):
        x += arr[i]
        y -= arr[i]
        a.add(arr[i])
        q = x - y

        if q % 2 != 0:
            continue
        elif q == 0 or (q > 0 and q / 2 in a):
            res = 'YES'
            break
    return res


n = int(input())
arr = list(map(int, input().split()))

res = f(arr, n)
if res == 'NO':
    arr = arr[::-1]
    res = f(arr, n)

print(res)
