(N, A, B) = list(map(int, input().split()))


def f(a, b):
    return [p for p in [N - i * a + j for i in range(1, N // a + 1 if N % a > b - N // a else N // a) for j in range(1, a + 1)] + [j for j in range(b - N // a if N % a > b - N // a else b - N // a + 1, N - N // a * a + 1 if N % a > b - N // a else N - (N // a - 1) * a + 1)] + [j for j in reversed(list(range(1, b - N // a if N % a > b - N // a else b - N // a + 1)))]]


ans = -1 if A * B < N or A + B > N + 1 else ' '.join((str(p) if A >= B else str(N - p + 1) for p in f(max(A, B), min(A, B))))
print(ans)
