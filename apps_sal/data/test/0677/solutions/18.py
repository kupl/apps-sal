q = int(input())
for c in range(q):
    (l, r, d) = map(int, input().split())
    if l > d:
        print(d)
    else:
        print(r + (d - r % d))
