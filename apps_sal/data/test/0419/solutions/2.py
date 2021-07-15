def mp():
    return map(int, input().split())

n = int(input(), 2)
ans = 0
i = 1
while i < n:
    i *= 4
    ans += 1

print(ans)
