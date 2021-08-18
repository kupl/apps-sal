import bisect
N, K = list(map(int, input().split()))
A = list(map(int, input().split()))


def divisor_all(n):
    l = [1, n]
    for i in range(2, int(pow(n, 1 / 2)) + 1):
        if n % i == 0:
            if i == n // i:
                l.append(i)
            else:
                l.append(i)
                l.append(n // i)
    l.sort(reverse=True)
    return l


D = divisor_all(sum(A))


def accumulater1D(A):
    B = [0] * len(A)
    B[0] = A[0]
    for i in range(1, len(B)):
        B[i] = B[i - 1] + A[i]
    return B


ans = 0

for d in D:
    R = [A[i] % d for i in range(N) if A[i] % d != 0]
    nr = len(R)

    R.sort()
    if len(R) == 0:
        ans = d
        break
    LR = accumulater1D(R)
    RR = list(reversed(accumulater1D([d - R[nr - 1 - i] for i in range(nr)])))

    for i in range(nr - 1):
        if LR[i] == RR[i + 1]:
            if LR[i] <= K:
                ans = d
                break
    if ans != 0:
        break
print(ans)
