h = int(input())
ans = 0
e = 1
while h > 0:
    ans += e
    e *= 2
    h = h // 2
print(ans)
