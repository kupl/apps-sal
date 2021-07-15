a, b, c, d = map(int, input().split())
if a < c:
        if b < c:
                print(0)
        if c <= b <= d:
                print(abs(b-c))
        if d < b:
                print(abs(d-c))
if c <= a:
        if d < a:
                print(0)
        if a <= d <= b:
                print(abs(d-a))
        if b < d:
                print(abs(b-a))
