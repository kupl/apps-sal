inp = [int(x) for x in input().split()]
x = sum(inp)
if x == 0:
    print(-1)
elif x % 5 == 0:
    print(x // 5)
else:
    print(-1)
