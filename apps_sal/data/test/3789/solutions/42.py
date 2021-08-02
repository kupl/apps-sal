N = int(input())
As = list(map(int, input().split()))


def func(Bs):
    for x in range(N):
        if Bs[x] >= 0: continue
        if max(Bs[x::x + 1]) <= 0:
            Bs[x] = 0


func(As)

zs = [27, 29, 31, 33] + list(range(34, 51))
for x in zs:
    if sum(As[x - 1::x]) < 0:
        for i in range(x - 1, N, x):
            As[i] = 0

ns = [1, 2, 4, 8, 16, 32] + [3, 6, 9, 12, 18, 24, 27, 36, 48] \
    + [5, 10, 15, 20, 25, 30, 40, 45, 50] + [7, 14, 21, 28, 35, 42, 49] \
    + [11, 22, 33, 44] + [13, 26, 39] + [17, 34] + [19, 38] + [23, 46] \
    + [29, 31, 37, 41, 43, 47]

memo = {}
memo[tuple(As)] = sum(As)

cs = [n - 1 for n in ns if n <= N and n not in zs and As[n - 1] < 0]
for c in cs:
    for tupleA in list(memo.keys()):
        if tupleA[c] == 0:
            continue

        listA = list(tupleA)
        for x in range(c, N, c + 1):
            listA[x] = 0

        func(listA)
        memo[tuple(listA)] = sum(listA)

print((max(memo.values())))
