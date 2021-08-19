(A, B, X) = map(int, input().split())
(l, r) = (0, 10 ** 9 + 1)
while r - l > 1:
    m = (l + r) // 2
    if A * m + B * len(str(m)) > X:
        r = m
    else:
        l = m
print(l)
