
import numpy as np

N, S = list(map(int, input().split()))
A = list(map(int, input().split()))

MOD = 998244353


def add_elements(w, i):
    a = A[i]
    w[a:] += w[:-a].copy()
    if a <= S:
        w[a] += i + 1
    w %= MOD


def main():
    w = np.zeros(S + 1, dtype=int)
    ans = 0
    for i in range(N):
        add_elements(w, i)
        ans = (ans + w[S]) % MOD

    print(ans)


def __starting_point():
    main()


__starting_point()
