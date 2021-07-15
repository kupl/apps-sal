a, b = map(int, input().split())
cnt = 1
plg = 0
while cnt < b:
    cnt -= 1
    cnt += a
    plg += 1
print(plg)
