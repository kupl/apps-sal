a, b, c = map(int, input().split())
d, e, f = map(int, input().split())
g, h, i = map(int, input().split())

if a + e + i == b + f + g == c + d + h == a + f + h == c + e + g == b + d + i:
    print("Yes")
else:
    print("No")
