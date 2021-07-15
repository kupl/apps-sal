n, x = map(int, input().split())
l = list(map(int, input().split()))
ans = 1
p = 0

for i in range(n):
    p += l[i]
    if p <= x:
        ans += 1
    else:
        break

print(ans)
