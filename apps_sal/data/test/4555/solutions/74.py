A, B, K = list(map(int, input().split()))
S = sorted(list(set([i for i in range(A, min(A + K, B))] + [i for i in range(max(A, B - K + 1), B + 1)])))
for s in S:
    print(s)

