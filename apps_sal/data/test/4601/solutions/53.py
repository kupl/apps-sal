(N, K) = list(map(int, input().split()))
H = sorted(list(map(int, input().split())), reverse=True)
if N <= K:
    print(0)
else:
    print(sum(H[K:]))
