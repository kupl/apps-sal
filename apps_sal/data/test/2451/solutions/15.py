n, h, a, b, k = tuple(map(int, input().split()))

for _ in range(k):
    fa, ta, fb, tb = tuple(map(int, input().split()))
    s = abs(fa - fb) + abs(ta - tb)
    if fa != fb:
        if ta < a and tb < a:
            s += 2 * min(a - ta, a - tb)
        if ta > b and tb > b:
            s += 2 * min(ta - b, tb - b)
    print(s)
