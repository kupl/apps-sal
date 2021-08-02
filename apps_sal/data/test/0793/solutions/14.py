def main():
    mod = 10**9 + 7
    N, M = map(int, input().split())
    S = list(map(int, input().split()))
    T = list(map(int, input().split()))
    V = [1] * N
    for t in T:
        p, q = 1, 1
        for i, (s, v) in enumerate(zip(S, V)):
            V[i] = q = v + q if s == t else v + q - p
            p = v
    return V[-1] % mod


print(main())
