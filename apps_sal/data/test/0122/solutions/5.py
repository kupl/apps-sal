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

# arr = list(map(int, input().split()))
# res = 0
# a = {math.pow(2, i) for i in range(35)}
# for i in range(n-1):
#     for j in range(i+1,n):
#         if arr[i] + arr[j] % 2 % 2 % 2 % 2 % 2 in a:
#             res += 1
#
# print(res)


# arr = list(map(int, input().split()))
# m = int(input())
# spis = list(map(int, input().split()))
#
# arr1 = sorted(arr, reverse=True)
# a = [n - arr1.index(arr[el - 1]) for el in spis]
# print(' '.join(map(str, a)))
