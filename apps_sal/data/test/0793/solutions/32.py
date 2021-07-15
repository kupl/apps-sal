def main():
    mod = 10**9 + 7
    N, M = list(map(int, input().split()))
    S = list(map(int, input().split()))
    T = list(map(int, input().split()))
    u = [1] * (N + 1)
    v = [1] * (N + 1)
    for t in T:
        for i, s in enumerate(S, 1):
            if s == t:
                v[i] = v[i - 1] + u[i]
            else:
                v[i] = v[i - 1] + u[i] - u[i - 1]
        u, v = v, u
    return u[-1] % mod

print((main()))

