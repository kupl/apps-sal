a, b, c = [int(i) for i in input().split()]
print(min((a + b) * 2, a + b + c, (a + c) * 2, (b + c) * 2))
