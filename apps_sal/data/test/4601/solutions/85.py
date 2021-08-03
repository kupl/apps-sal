N, K = map(int, input().split())
H = list(map(int, input().split()))
if N <= K:
    print(0)
else:
    H.sort(reverse=True)
    for i in range(K):
        H[i] = 0
    print(sum(H))
