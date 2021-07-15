n = int(input())
p = list(map(int,input().split()))
min = p[0]
ans = 0
for i in range(n):
    if min >= p[i]:
        ans += 1
        min = p[i]
print(ans)
