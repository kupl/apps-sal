N = int(input())
TA = [list(map(int, input().split())) for _ in range(N)]
(T, A) = (0, 0)
for (t, a) in TA:
    if T == 0 and A == 0:
        T = t
        A = a
        continue
    if t == a:
        M = max(T, A)
        T = M
        A = M
    elif t < a:
        n = max(T // t * t, A // a * t)
        while n < T or a * (n // t) < A:
            n += t
        T = n
        A = a * (T // t)
    else:
        n = max(A // a * a, T // t * a)
        while n < A or t * (n // a) < T:
            n += a
        A = n
        T = t * (A // a)
print(A + T)
