(A, B, X) = [int(_) for _ in input().split()]


def d(N):
    return len(str(N))


ok_max = 0
ng_min = 10 ** 9 + 1
while ng_min - ok_max > 1:
    n = (ok_max + ng_min) // 2
    if A * n + B * d(n) <= X:
        ok_max = n
    else:
        ng_min = n
print(ok_max)
