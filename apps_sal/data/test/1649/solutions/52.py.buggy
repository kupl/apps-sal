*a, = map(int, input().split())
for s in range(1 << 4):
    x = 0
    for i in range(4):
        if (1 << i) & s:
            x += a[i]
    if 2 * x == sum(a):
        print("Yes")
        return
print("No")
