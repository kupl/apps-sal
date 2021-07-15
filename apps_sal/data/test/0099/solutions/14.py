b, q, l, m = list(map(int, input().split()))
bad = set(map(int, input().split()))

cnt = 0

if abs(b) > l:
    print(0)
elif q == 0 or b == 0:
    if b not in bad:
        cnt += 1
    if 0 in bad:
        print(cnt)
    else:
        print("inf")
elif abs(q) == 1:
    if b in bad and (q == 1 or -b in bad):
        print(0)
    else:
        print("inf")
else:
    while abs(b) <= l:
        if b not in bad:
            cnt += 1
        b *= q
    print(cnt)

