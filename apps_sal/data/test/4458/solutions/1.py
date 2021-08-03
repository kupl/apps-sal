n = int(input())
p = list(map(int, input().split()))

ans = 0
m = p[0]

for i in p:
    if m >= i:
        ans += 1
        m = i

print(ans)
