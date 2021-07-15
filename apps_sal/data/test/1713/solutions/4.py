
n, a, b = map(int, input().split())
t = [0] + list(map(int, input().split()))

if a == b: print(0)
else:
    x, s = t[a], 1

    while x != b and x != a:
        x = t[x]
        s += 1
    if x == a: print(-1)
    else: print(s)
