(a, b) = map(int, input().split())
ans = 0
outlet = 1
while outlet < b:
    outlet -= 1
    outlet += a
    ans += 1
print(ans)
