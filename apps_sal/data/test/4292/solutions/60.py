n, k = map(int, input().split())
P = list(map(int, input().split()))
P.sort()
print(sum(P[:k]))
