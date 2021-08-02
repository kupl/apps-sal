N, A, B = [int(_) for _ in input().split()]
if N < A + B - 1 or A * B < N:
    print((-1))
elif B == 1:
    print((*list(range(1, A + 1))))
else:
    M = N - A - B + 1
    count = [B] * (1 + M // (B - 1))
    count += [1] * (A - len(count))
    count[-1] += (N - A - B + 1) % (B - 1)
    f = 0
    ans = []
    for c in count:
        ans += list(range(f + c, f, -1))
        f += c
    print((*ans))
