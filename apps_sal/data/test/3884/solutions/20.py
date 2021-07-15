rd = lambda: list(map(int, input().split()))
n, m = rd(), rd()[0]
r = m
for x in rd() + rd():
    if x > 1:
        r *= x
        r /= x - 1
    else:
        print(-1)
        return
print(r - m)

