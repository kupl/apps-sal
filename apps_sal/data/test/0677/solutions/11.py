q = int(input())

for _ in range(q):
    l, r, d = map(int, input().split())
    if d < l:
        print(d)
    else:
        print((r // d + 1) * d)
