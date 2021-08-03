a, b, c = list(map(int, input().split()))

n = b // a
if n >= c:
    print(c)
else:
    print(n)
