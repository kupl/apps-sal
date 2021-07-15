a, b, c = map(int, input().split())

n = b // a
if n < c:
    print(n)
else:
    print(c)
