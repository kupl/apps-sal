N = int(input())
P = [int(i) for i in input().split()]
p = N
ans = 0
for i in range(N):
    if p >= P[i]:
        ans += 1
        p = P[i]
print(ans)
