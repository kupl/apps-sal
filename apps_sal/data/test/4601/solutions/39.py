(N, K) = map(int, input().split())
H = list(map(int, input().split()))
H.sort(reverse=True)
print(max(0, sum(H[K:])))
