N, K = map(int, input().split())
L = list(map(int, input().split()))

L.sort()
L.reverse()

print(sum(L[:K]))
