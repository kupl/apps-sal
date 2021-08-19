(n, l) = map(int, input().split())
m = list(range(l, l + n))
if m[-1] < 0:
    print(sum(m[:n - 1]))
elif m[0] > 0:
    print(sum(m[1:]))
else:
    print(sum(m))
