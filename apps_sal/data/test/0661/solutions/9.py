m, k = map(int, input().split())
if m == 0:
    if k == 0:
        print(0, 0)
    else:
        print(-1)
    return
if m == 1:
    if k == 0:
        print(0, 0, 1, 1)
    else:
        print(-1)
    return
if k < 2**m:
    l = [i for i in range(2**m) if i != k]
    l = l + [k] + l[::-1] + [k]
    print(*l)
else:
    print(-1)
