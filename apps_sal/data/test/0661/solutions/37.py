from itertools import chain
m, k = map(int, input().split())
if k == 0:
    print(" ".join([str(i) for i in chain(range(0, 2**m), range(2**m - 1, -1, -1))]))
elif 0 < k < 2**m:
    s = 0
    for i in range(0, 2**m):
        if i != k:
            s ^= i
    if s == k:
        print(" ".join([str(i) for i in chain(range(0, k), range(k + 1, 2**m), [k], range(2**m - 1, k, -1), range(k - 1, -1, -1), [k])]))
    else:
        print(-1)
else:
    print(-1)
