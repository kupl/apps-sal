import sys
input = sys.stdin.readline
n = int(input())
A = [int(i) for i in input().split()]
A.sort()
ans = 1
cur = max(1, A[0] - 1)
for i in range(1, n):
    a = A[i]
    if a < cur:
        continue
    elif a == cur:
        ans += 1
        cur += 1
    elif a > cur + 1:
        ans += 1
        cur = a - 1
    else:
        ans += 1
        cur = a
print(ans)
