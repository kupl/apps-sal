from heapq import heappush, heappop, heappushpop
N = int(input())
A = [int(a) for a in input().split()]


def calc(L):
    s = sum(L[:N])
    h = []
    X = [s]
    for i in range(N):
        heappush(h, L[i])
    for i in range(N, 2 * N):
        s += L[i] - heappushpop(h, L[i])
        X.append(s)
    return X


B = calc(A)
C = calc([-a for a in A][::-1])[::-1]
print(max([B[i] + C[i] for i in range(N + 1)]))
