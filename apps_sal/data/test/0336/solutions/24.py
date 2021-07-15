n, a, b, c, d = list(map(int, input().split(' ')))
print(max(0, n*(n-max([a+b, a+c, c+d, b+d])+min([a+b, a+c, c+d, b+d]))))

