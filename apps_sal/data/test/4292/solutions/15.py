(n, k) = map(int, input().split())
l = list(map(int, input().split()))
l = sorted(l)[:k]
print(sum(l))
