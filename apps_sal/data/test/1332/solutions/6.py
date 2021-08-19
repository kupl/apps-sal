x = sum(map(int, str.split(input())))
if x > 0 and x % 5 == 0:
    print(x // 5)
else:
    print(-1)
