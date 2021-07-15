n, p = int(input()), sorted((x, i) for i, x in enumerate(map(int, input().split())))
print(p[-1][1] + 1, p[-2][0])
