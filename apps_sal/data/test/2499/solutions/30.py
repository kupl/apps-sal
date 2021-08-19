N = int(input())
A = list(map(int, input().split()))
ans = 0
for a in A:
    ans ^= a
for i in range(N):
    A[i] &= ~ans


def gauss_jordan(bs):
    rank = 0
    pivot_cols = []
    for col in reversed(range(61)):
        pivot = -1
        for (i, row) in enumerate(bs[rank:]):
            if row & 1 << col:
                pivot = rank + i
                break
        if pivot < 0:
            continue
        pivot_cols.append(col)
        (bs[pivot], bs[rank]) = (bs[rank], bs[pivot])
        for (i, row) in enumerate(bs):
            if i != rank and row & 1 << col:
                bs[i] ^= bs[rank]
        rank += 1
    return (pivot_cols, bs)


(pivot_cols, bs) = gauss_jordan(A)
x = 0
for j in reversed(range(61)):
    nx = x | 1 << j
    b = nx
    for (i, c) in enumerate(pivot_cols):
        if b & 1 << c:
            b ^= bs[i]
    if b & nx == 0:
        x = nx
ans += x * 2
print(ans)
