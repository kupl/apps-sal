N, K = list(map(int, input().split()))

ns = {x for x in range(1, N + 1)}

for _ in range(K):
    _ = input()
    ns -= set(map(int, input().split()))

print((len(ns)))
