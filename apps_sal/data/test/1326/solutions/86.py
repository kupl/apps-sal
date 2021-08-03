import sys
N = int(sys.stdin.readline())
# ans=sum((N//x)*(N//x+1)*x//2 for x in range(1,N+1))
ans = 0
for x in range(1, N + 1):
    y = N // x
    ans += y * (y + 1) * x // 2
print(ans)
