import copy
n = int(input())
p = list(map(int, input().split()))

A = copy.copy(p)
A.sort()
cnt = 0

for i in range(n):
    if A[i] != p[i]:
        cnt += 1

if cnt == 2 or cnt == 0:
    print('YES')
else:
    print('NO')
