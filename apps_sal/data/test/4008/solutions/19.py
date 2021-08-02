import sys
N, K = list(map(int, input().split()))
A = [int(i) for i in input().split()]
L = [0] * (5001)
num = [0] * (5001)
for a in A:
    num[a] += 1
for s in num:
    if s > K:
        print('NO')
        return
table = []
for i in range(N):
    table.append((A[i], i))
table.sort()
ans = [0] * N
# print(table)
t = 0
for a, i in table:
    t += 1
    if t % K != 0:
        ans[i] = t % K
    else:
        ans[i] = K
print('YES')
print(' '.join(map(str, ans)))
