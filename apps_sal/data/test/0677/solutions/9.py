q = int(input())
for i in range(q):
    (a, b, d) = map(int, input().split())
    if d < a:
        print(d)
    else:
        print(b // d * d + d)
