m, k = list(map(int, input().split()))
if k >= 2**m:
    print((-1))
elif m == 1:
    if k == 0: print((0, 0, 1, 1))
    else: print((-1))
else:
    tmp = k
    for i in range(1, 2**m):
        tmp ^= i
    ans = [i for i in range(2**m) if i != k] + [k] + [i for i in range(2**m - 1, -1, -1) if i != k] + [k]
    print((*ans))
