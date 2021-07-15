a, b, c = map(int, input().split())
M = max(a, b, c)
r = a+b+c-M

print(10*M + r)
