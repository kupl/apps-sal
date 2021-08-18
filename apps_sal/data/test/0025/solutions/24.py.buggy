import math
import re


n, k = list(map(int, input().split()))


if k > n * n:
    print(-1)
    return

a = [[0] * n for i in range(n)]

for i in range(n):
    if k == 0:
        break
    a[i][i] = 1
    k -= 1
    if k == 0:
        break
    elif k == 1:
        a[i + 1][i + 1] = 1
        break
    else:
        for j in range(i + 1, min(n, i + 1 + k // 2)):
            a[i][j] = 1
            a[j][i] = 1
            k -= 2


for i in range(n):
    print(' '.join(map(str, a[i])))


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
