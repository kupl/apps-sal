import sys
input = sys.stdin.readline
(n, m) = list(map(int, input().split()))
mex = []
for i in range(m):
    mex.append(list(map(int, input().split())))
ans = min([j - i + 1 for (i, j) in mex])
print(ans)
lis = []
for i in range(n):
    lis.append(str(i % ans))
print(' '.join(lis))
