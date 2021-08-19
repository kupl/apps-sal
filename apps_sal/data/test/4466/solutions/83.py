(x, y, z) = (int(i) for i in input().split())
ans = 0
while True:
    x -= y + z
    if x - z >= 0:
        ans += 1
    else:
        break
print(ans)
