a, b, c = list(map(int, input().split()))
print(min(a+b, b+c, c+a, (a+b+c)//3))


