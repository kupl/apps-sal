import collections
import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
m = 1000000007

flag0 = 1
count = 0
# 偶数だったら
if N % 2 == 0:
    colA = collections.Counter(A)
    for key, val in list(colA.items()):
        if key % 2 != 1 or val != 2:
            flag0 = 0
            break
    for i in range(1, N, 2):
        if i not in list(colA.keys()):
            flag = 0
            break
        else:
            count += 1
# 奇数だったら
else:
    A.append(0)
    colA = collections.Counter(A)
    for key, val in list(colA.items()):
        if key % 2 != 0 or val != 2:
            flag0 = 0
            break
    for i in range(0, N, 2):
        if i not in list(colA.keys()):
            flag = 0
            break
        else:
            count += 1
    count -= 1


print((((2**count) % m) * flag0))
