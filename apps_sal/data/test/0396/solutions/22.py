dtnums = []
for x in range(0,40):
    for y in range(0,40):
        dtnums.append((2**x)*(3**y))

x, y = map(int, input().split())
ans = 0
for i in dtnums:
    if x <= i <= y:
        ans += 1
print(ans) 
