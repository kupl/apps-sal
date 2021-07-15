N = int(input())
d  = [int(n) for n in input().split()]

ans = 0
for i in range(N-1):
    for j in range(i+1, N):
        ans += d[i] * d[j]

print(ans)
