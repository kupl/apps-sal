(a, b, c, d) = list(map(int, input().split()))
x = max(a, b, c, d)
if x == a:
    print(x - b, x - c, x - d)
elif x == b:
    print(x - a, x - c, x - d)
elif x == c:
    print(x - b, x - a, x - d)
elif x == d:
    print(x - b, x - c, x - a)
