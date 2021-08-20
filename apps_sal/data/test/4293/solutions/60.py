(a, b, c) = map(int, input().split())
x = []
x.append(a + b)
x.append(a + c)
x.append(b + c)
print(sorted(x)[0])
