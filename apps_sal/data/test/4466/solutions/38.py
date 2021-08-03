x, y, z = map(int, input().split())
x -= y + 2 * z
ans = 1
while x - (y + z) >= 0:
    ans += 1
    x -= y + z
print(ans)
