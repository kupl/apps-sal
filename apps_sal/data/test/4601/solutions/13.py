N, K = map(int, input().split())
H = list(map(int, input().split()))
H.sort()
m = 0
if K < N:
    for i in range(N - K):
        m += H[i]
print(m)
