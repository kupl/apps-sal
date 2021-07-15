N = int(input())
s = list(map(int, input().split()))
ans = 0
for C in range(1,N):
    t = 0
    for x in range(C, N-1-C if (N-1)%C != 0 else N//2, C):
        t += s[x] + s[-x-1]
        ans = max(ans, t)
print(ans)
