Q = int(input())
for _ in range(Q):
    N, K = list(map(int, input().split()))
    S = input()
    X = [{"R": 0, "G": 1, "B": 2}[s] for s in S]
    mi = K
    for i in range(3):
        d = 0
        for j in range(N):
            if X[j] != (i + j) % 3:
                d += 1
            if j >= K and X[j - K] != (i + j - K) % 3:
                d -= 1
            if j >= K - 1:
                mi = min(mi, d)
    print(mi)
