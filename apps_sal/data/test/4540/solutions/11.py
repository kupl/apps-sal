N = int(input())
A = list((int(a) for a in input().split()))
A = [0] + A + [0]
dist = [0]
for i in range(1, N + 2):
    dist.append(abs(A[i] - A[i - 1]))
dist_cum = [0] * (N + 2)
for i in range(N + 1):
    dist_cum[i + 1] = dist_cum[i] + dist[i + 1]
for i in range(1, N + 1):
    if A[i - 1] < A[i] and A[i] < A[i + 1]:
        print(dist_cum[-1])
    elif A[i - 1] > A[i] and A[i] > A[i + 1]:
        print(dist_cum[-1])
    else:
        tmp = dist_cum[i - 1]
        tmp += dist_cum[-1] - dist_cum[i + 1]
        tmp += abs(A[i + 1] - A[i - 1])
        print(tmp)
