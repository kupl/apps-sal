(n, c) = (int(input()), 0)
a = list(map(int, input().split()))
(x, f) = map(int, input().split())
for i in a:
    if i > x:
        if (i - x) % (x + f) == 0:
            c += (i - x) // (x + f)
        else:
            c += (i - x) // (x + f) + 1
print(c * f)
