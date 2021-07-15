def f_contrast():
    from collections import Counter
    N = int(input())
    A = [int(i) for i in input().split()]
    B = [int(i) for i in input().split()]

    c = [0] * (N + 1)
    d = [0] * (N + 1)

    for a, b in zip(A, B):
        c[a] += 1
        d[b] += 1

    for s, t in zip(c, d):
        if s + t > N:
            return 'No'

    for i in range(1, N + 1):
        c[i] += c[i - 1]
        d[i] += d[i - 1]

    shift = max(c[i] - d[i - 1] for i in range(1, N + 1))
    ans = [B[(i + N - shift) % N] for i in range(N)]
    ret = ' '.join(map(str, ans))
    return f'Yes\n{ret}'

print(f_contrast())
