def upper_bound(A, x):
    (s, t) = (-1, len(A))
    while t - s > 1:
        m = (s + t) // 2
        if A[m] > x:
            t = m
        else:
            s = m
    return t


def lower_bound(A, x):
    (s, t) = (-1, len(A))
    while t - s > 1:
        m = (s + t) // 2
        if A[m] >= x:
            t = m
        else:
            s = m
    return t


N = int(input())
A = sorted(list(map(int, input().split())))
B = sorted(list(map(int, input().split())))
C = sorted(list(map(int, input().split())))
ans = 0
for b in B:
    ans += lower_bound(A, b) * (N - upper_bound(C, b))
print(ans)
