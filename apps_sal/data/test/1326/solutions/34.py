import numpy as np
from numba import njit


@njit
def main(N):
    spf = np.zeros(N + 1, np.int32)
    prime = np.zeros(N + 1, np.int32)
    index = 0
    for i in range(2, N + 1):
        if not spf[i]:
            spf[i] = i
            prime[index] = i
            index += 1
        for j in range(index):
            if prime[j] > i or i * prime[j] > N:
                break
            spf[i * prime[j]] = prime[j]
    ans = 0
    for k in range(1, N + 1):
        n = k
        before = spf[n]
        count = 0
        fk = 1
        while n > 1:
            if spf[n] == before:
                count += 1
                n //= spf[n]
            else:
                fk *= count + 1
                before = spf[n]
                count = 1
                n //= spf[n]
        fk *= count + 1
        ans += k * fk
    print(ans)


N = int(input())
main(N)
