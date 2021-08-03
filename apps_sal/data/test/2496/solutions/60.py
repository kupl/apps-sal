def divplis(N):
    lis = [i for i in range(N + 1)]
    for i in range(int(N**0.5 + 1), 1, -1):
        if lis[i] == i:
            lis[i::i] = [i] * (N // i)
    return lis


divp = divplis(10**6 + 1)
N = int(input())
d = [0] * (10**6 + 1)
A = [int(i) for i in input().split()]


def pfact(N):
    b = 0
    while N != 1:
        n = divp[N]
        if b != n:
            d[n] += 1
        b = n
        N = N // n
    return 0


for a in A:
    pfact(a)
m = max(d)
if m <= 1:
    print("pairwise coprime")
elif m == N:
    print("not coprime")
else:
    print("setwise coprime")
