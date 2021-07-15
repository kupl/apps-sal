n = int(input())
p = list(map(int,input().split()))
min_p = n+1
ans = 0
for i in range(n):
    if p[i] < min_p:
        ans += 1
        min_p = p[i]
print(ans)
