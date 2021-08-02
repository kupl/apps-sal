a, b, c = map(int, input().split())
s = []
s.append(a + b)
s.append(a + c)
s.append(b + c)


print(min(s))
