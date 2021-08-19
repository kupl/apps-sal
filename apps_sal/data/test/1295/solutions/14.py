def UpperBound(A, key):
    left = -1
    right = len(A)
    while right > left + 1:
        middle = (left + right) // 2
        if A[middle] > key:
            right = middle
        else:
            left = middle
    return right


def LowerBound(A, key):
    left = -1
    right = len(A)
    while right > left + 1:
        middle = (left + right) // 2
        if A[middle] >= key:
            right = middle
        else:
            left = middle
    return right


n, m = map(int, input().split())
N = list(map(int, input().split()))
M = list(map(int, input().split()))
INF = 10**9

dist = [INF] * (n)
min_dist = 0

for i in range(n):
    l = LowerBound(M, N[i])
    if l > len(M) - 1:
        l = len(M) - 1

    d1 = abs(N[i] - M[l])
    # print(d1)
    if 0 < l:
        d2 = abs(N[i] - M[l - 1])
        # print(d2)
    else:
        d2 = d1
    dist[i] = min(d1, d2)

print(max(dist))
