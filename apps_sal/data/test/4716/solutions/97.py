N, K = list(map(int, input().split()))
L = list(map(int, input().split()))

L.sort()
print((sum(L[-K:])))
