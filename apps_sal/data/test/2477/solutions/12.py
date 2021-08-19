(N, K) = list(map(int, input().split()))
A = list(map(int, input().split()))
(l, r) = (0, 10 ** 9)
while r - l > 1:
    x = (r + l) // 2
    c = 0
    for a in A:
        c += (a - 1) // x
    if c <= K:
        r = x
    else:
        l = x
print(r)
