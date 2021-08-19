N = int(input())
A = list(map(int, input().split()))
NN = ((N + 1) * N // 2 + 1) // 2


def ok(x):
    B = [0] * (2 * N + 1)
    (res, cum, cur) = (0, 0, 0)
    B[0] += 1
    for a in A:
        if a >= x:
            cum += 1
            cur += B[cum] + 1
        else:
            cur -= B[cum] - 1
            cum -= 1
        B[cum] += 1
        res += cur
    return res >= NN


B = sorted(set(A))
l = 0
r = len(B)
while r - l > 1:
    m = (l + r) // 2
    if ok(B[m]):
        l = m
    else:
        r = m
print(B[l])
