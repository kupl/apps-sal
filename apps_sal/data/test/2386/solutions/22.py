import sys
input = sys.stdin.readline
N = int(input())
A = list(map(int, input().split()))
for i in range(N):
    A[i] -= i + 1
A.sort()
ans = float('inf')
cand = [A[N // 2]]
if N > 1:
    cand.append(A[N // 2 + 1])
for i in cand:
    tmp = 0
    for a in A:
        tmp += abs(a - i)
    ans = min(ans, tmp)
print(ans)
