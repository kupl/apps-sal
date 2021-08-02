m, k = list(map(int, input().split()))
if 2**m <= k: print((-1)); return
if m == 1:
    if k == 0: print((0, 0, 1, 1))
    else: print((-1))
    return
a = [i for i in range(2**m) if i != k]
ans = [k] + a + [k] + a[::-1]
print((*ans))
