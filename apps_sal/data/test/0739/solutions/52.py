import math
import sys
sys.setrecursionlimit(10000)


def nasu(A, B, L, D, M):
    if L == 1:
        return A
    ans = nasuA(A, L, D, M)
    ans = (ans + nasuB(1, L - 1, D, M) * B * D) % M
    return ans % M


def nasuB(B, L, D, M):
    if L == 1:
        return B
    ans = powB(1, L, D, M) % M
    return ans % M


def powB(B, L, D, M):
    if L == 1:
        return B
    k = 0
    t = D
    while T[k + 1] <= L:
        k += 1
        t = t * t % M
        if k + 1 == len(T):
            break
    ans = powB2(B, T[k], D, M) % M
    if L != T[k]:
        ans += nasu(T[k] + 1, 1, L - T[k], D, M) * t % M
    return ans % M


def powB2(B, L, D, M):
    if L == 1:
        return 1
    ans = powB2(B * 2, L // 2, D * D % M, M) * (D + 1) % M
    ans = ans + nasuA(1, L // 2, D * D % M, M) * B * D % M
    return ans


def nasuA(A, L, D, M):
    if L == 1:
        return A
    ans = powA(A, L, D, M) % M
    return ans % M


def powA(A, L, D, M):
    if L == 1:
        return A
    k = 0
    t = D
    while T[k + 1] <= L:
        k += 1
        t = t * t % M
        if k + 1 == len(T):
            break
    ans = powA2(A, T[k], D, M)
    if L != T[k]:
        ans += powA(A, L - T[k], D, M) * t % M
    return ans % M


def powA2(A, L, D, M):
    if L == 1:
        return A
    return powA2(A, L // 2, D * D % M, M) * (D + 1) % M


def powmod(a, n, M):
    ans = 1
    while n:
        if n & 1:
            ans = ans * a % M
        a = a * a % M
        n >>= 1
    return ans


(L, A, B, M) = list(map(int, input().split()))
N = math.ceil(math.log(A + 1, 10))
k = pow(10, N)
D = [[0, 0] for _ in range(20)]
while L > 0:
    n = min(L, (k - 1 - A) // B + 1)
    D[N - 1][0] = A
    D[N - 1][1] = n
    L -= n
    N += 1
    k *= 10
    A += n * B
T = [1]
while T[-1] < 10 ** 19:
    T.append(T[-1] * 2)
BI = ((B // M + 1) * M - B) % M
ans = 0
for i in range(20):
    l = D[i][1]
    a = D[i][0] + (l - 1) * B
    if l == 0:
        continue
    ans = ans * powmod(pow(10, i + 1), l, M) % M
    ans = (ans + nasu(a, BI, l, pow(10, i + 1), M)) % M
print(ans)
