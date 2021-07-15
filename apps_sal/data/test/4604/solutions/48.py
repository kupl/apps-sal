from collections import defaultdict
N = int(input())
A = list(map(int, input().split()))

L = A[:]
L = list(set(L))

mod = 10 ** 9 + 7

d = defaultdict(int)
for i in range(N):
    d[A[i]] += 1

if N % 2 == 1:
    bfr = 0
    for i in L:
        if i - bfr != 2 and i != 0:
            print((0))
            return

        if i == 0:
            if d[i] != 1:
                print((0))
                return
            else:
                continue
        if d[i] != 2:
            print((0))
            return
        bfr = i

    print(((2 ** (N // 2)) % mod))
else:
    bfr = 1
    for i in L:
        if i - bfr != 2 and i != 1:
            print((0))
            return

        if d[i] != 2:
            print((0))
            return
        bfr = i

    print(((2 ** (N // 2)) % mod))

