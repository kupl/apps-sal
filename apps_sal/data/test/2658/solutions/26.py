import numpy as np


def main():
    (N, K) = map(int, input().split())
    A = [0]
    A += list(map(int, input().split()))
    A = np.array(A)
    i = 1
    pas = np.zeros(N)
    pas[0] = i
    k = 1
    pass_set = set(pas)
    while k <= K:
        if A[i] in pass_set:
            rps = np.where(pas == A[i])[0]
            ans = A[i]
            break
        pas[k] = A[i]
        pass_set.add(A[i])
        ans = A[i]
        i = A[i]
        k += 1
    if k >= K:
        print(ans)
    else:
        rpnum = (K - rps[0]) % (k - rps)
        print(int(pas[rps[0] + rpnum]))


main()
