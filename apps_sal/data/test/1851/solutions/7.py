N = int(input())
A = [int(a) - 1 for a in input().split()]
ma = 0
ans = 0
for i in range(N):
    ma = max(ma, A[i])
    if ma <= i:
        ans += 1
print(ans)
