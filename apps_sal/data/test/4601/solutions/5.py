N, K = map(int, input().split())
H = list(map(int, input().split()))

H.sort(reverse=True)

if K <= len(H):
    print(sum(H[K:len(H) + 1]))
else:
    print(0)
