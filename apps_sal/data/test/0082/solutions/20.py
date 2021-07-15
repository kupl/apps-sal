import math
import re

def f(n):
    if n - math.floor(n) < 0.5:
        return n
    else :
        return math.ceil(n)

n, k = list(map(int, input().split()))
a = list(map(int, input().split()))

n1 = n
s = sum(a)
sred = s/n
while f(sred) != k:
    s += k
    n += 1
    sred = s/n

print(n - n1)

# n, m = map(int, input().split())
# w = []
# c = []
# for i in range(n):
#     x, y = map(int, input().split())
#     w.append(x)
#     c.append(y)
#
# A = [[0] * (m + 1) for i in range(n)]
#
#
# for k in range(n):
#       for s in range(1, m + 1):
#             if s >= w[k]:
#                 A[k][s] = max(A[k - 1][s], A[k - 1][s - w[k]] + c[k])
#             else:
#                 A[k][s] = A[k-1][s]
#
# print(A[n - 1][m])

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

