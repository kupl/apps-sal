t = int(input())
for i in range(t):
    (l, r, d) = list(map(int, input().split()))
    if d < l:
        print(d)
    elif d > r:
        print(d)
    else:
        print((r // d + 1) * d)
