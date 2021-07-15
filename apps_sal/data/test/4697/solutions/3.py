s, c = map(int, input().split())
c = c//2

if s == c:
    print(s)
elif s > c:
    print(c)
elif s < c:
    t = c - s
    print(s + t//2)
