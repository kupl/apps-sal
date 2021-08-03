n, m, z = map(int, input().split())
c = n
ans = 0
while c <= z:
    if c % m == 0:
        ans += 1
    c += n
print(ans)
