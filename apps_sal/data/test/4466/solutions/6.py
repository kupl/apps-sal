x, y, z = map(int, input().split())
ans = 0
i = 1
while 1:
    haba = (i * y) + ((i + 1) * z)
    if haba > x:
        break
    else:
        ans = i
    i += 1

print(ans)
