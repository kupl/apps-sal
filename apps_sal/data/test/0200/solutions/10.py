(h1, h2) = map(int, input().split(' '))
h = h2 - h1
(a, b) = map(int, input().split())
h -= a * 8
if h <= 0:
    print(0)
elif a <= b:
    print(-1)
else:
    print(h // (12 * (a - b)) + (1 if h % (12 * (a - b)) else 0))
