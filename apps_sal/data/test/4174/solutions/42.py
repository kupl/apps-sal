n, x = map(int, input().split())
ans = 1
p = 0
l = [int(x) for x in input().split()]
for i in range(n):
    p += l[i]
    if p > x:
        break
    else:
        ans += 1

print(ans)
