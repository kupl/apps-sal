n, l = map(int, input().split())

apple = []
diff = 1001001001
minus = False
for i in range(1, n + 1):
    apple.append(l + i - 1)
    if abs(l + i - 1) < diff:
        diff = abs(l + i - 1)
        if l + i - 1 < 0:
            minus = True
        else:
            minus = False

if minus:
    print(sum(apple) + diff)
else:
    print(sum(apple) - diff)
