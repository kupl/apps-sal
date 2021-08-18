from copy import deepcopy
mex = ((1, 2, 1), (2, 0, 0), (1, 0, 0))
"""
import random
a= [[random.randrange(0,3) for _ in range(10)] for _ in range(10)]
for i in range(3,10):
    for j in range(3,10):
        a[i][j] = mex[a[i-1][j]][a[i][j-1]]"""
# n=10
n = int(input())
*a1, = list(map(int, input().split()))
a = [a1]
for _ in range(n - 1):
    a.append([int(input())])
ans = [0, 0, 0]
if n < 20:
    for i in range(1, n):
        for j in range(1, n):
            a[i].append(mex[a[i - 1][j]][a[i][j - 1]])
    for i in range(n):
        for j in range(n):
            ans[a[i][j]] += 1
    print((*ans))
    return


for i in range(1, 5):
    for j in range(1, n):
        a[i].append(mex[a[i - 1][j]][a[i][j - 1]])

for i in range(5, n):
    for j in range(1, 5):
        a[i].append(mex[a[i - 1][j]][a[i][j - 1]])

for i in range(5):
    for j in range(n):
        ans[a[i][j]] += 1
        ans[a[j][i]] += 1

for i in range(5):
    for j in range(5):
        ans[a[i][j]] -= 1


for j in range(4, n):
    ans[a[4][j]] += n - j - 1
    ans[a[j][4]] += n - j - 1
ans[a[4][4]] -= n - 5
print((*ans))
