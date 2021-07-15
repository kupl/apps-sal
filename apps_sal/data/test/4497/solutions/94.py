N = int(input())
print((max(2 ** i if 2 ** i <= N else 0 for i in range(10))))

