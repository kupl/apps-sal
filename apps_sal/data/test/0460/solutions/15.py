import math
import re
import random


def generator(s):
    a = []
    i = (s // 50) % 475
    for k in range(25):
        i = (i * 96 + 42) % 475
        a.append(26 + i)
    return a


p, x, y = list(map(int, input().split()))

ans = 10000000000000

for a in range(2000):
    for b in range(2000):
        k = x + 100 * a - 50 * b;
        if k >= y and p in generator(k):
            ans = min(ans, a);
            print(ans)
            return

print(ans)


# def func(arr, qb, allb, res):
#     for el in arr:
#         if el == 'b':
#             qb += 1
#         else:
#             allb += qb
#             qb = 0
#             res += allb
#             allb *= 2
#     return res
#
#
# arr = input()
#
#
# arr = arr[::-1]
#
# res = func(arr, 0, 0, 0)
#
# #print(res)
#
# print(res % (pow(10, 9) + 7))


# n = int(input())
#
#
# if n % 2 == 0:
#     print(n//2 - 1)
# else:
#     print(n//2)


#n = int(input())
# res = ''
# for i in range(n):
#     if i % 4 == 0 or i % 4 == 1:
#         res += 'a'
#     else:
#         res += 'b'
#
# print(res)


# l, r = map(int, input().split())
# if l == r and l % 2 != 0:
#     print(l)
# else:
#     print(2)


# n = int(input())
# a = list(map(len, input().replace('-', ' ').split()))
# for i in range(len(a) - 1):
#     a[i] += 1
#
#
#
#
#
# print(' '.join(map(str, a)))


# n = int(input())
# a = list(map(int, input().split()))
#
# b = []
# q = 0
# for i in range(n):
#     if a[i] != 0 and i != n-1:
#         q += 1
#     elif a[i] == 0 and i != n-1:
#        b.append(q)
#        q = 0
#     elif a[i] == 0 and i == n-1:
#         b.append(q)
#         b.append(0)
#         break
#     else:
#         q += 1
#         b.append(q)
#         break
#
#
# c = []
#
# for j in range(len(b)):
#     if j == 0:
#         for i in range(b[0]):
#             c.append(b[0] - i)
#         c.append(0)
#     elif j == len(b) - 1:
#         for i in range(b[j]):
#             c.append(i + 1)
#     else:
#
#         if b[j] % 2 == 0:
#             for i in range(b[j]//2):
#                 c.append(i + 1)
#             for i in range(b[j]//2):
#                 c.append(b[j]//2 - i)
#             c.append(0)
#         else:
#             for i in range(b[j]//2 + 1):
#                 c.append(i + 1)
#             for i in range(b[j]//2):
#                 c.append(b[j]//2 - i)
#             c.append(0)
#
#
# #print(' '.join(map(str, b)))
#
# print(' '.join(map(str, c)))


#print('2 1 0 1 0 0 1 2 3 ')


# n, k  = map(int, input().split())
#
#
# if k > n*n:
#     print (-1)
#     return
#
# a = [[0] * n for i in range(n)]
#
# for i in range(n):
#     if k == 0:
#         break
#     a[i][i] = 1
#     k -= 1
#     if k == 0:
#         break
#     elif k == 1:
#         a[i+1][i+1] = 1
#         break
#     else:
#         for j in range(i+1, min(n, i + 1 + k//2)):
#                        a[i][j] = 1
#                        a[j][i] = 1
#                        k -= 2
#
#
# for i in range(n):
#     print(' '.join(map(str, a[i])))


# n = int(input())
# a = list(map(int, input().split()))
# #print(' '.join(map(str, a)))
#
#
#
# b = set()
#
# for el in a:
#     if el-1 in b:
#         b.discard(el-1)
#         b.add(el)
#     else:
#         b.add(el)
#
# print(len(b))
