n = int(input())
lst = list(map(int, input().split()))

m = n+1
ans = 0

for i in lst:
    if i < m:
        ans += 1
        m = i

print(ans)
