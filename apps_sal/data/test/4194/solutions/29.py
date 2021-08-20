(n, m) = map(int, input().split())
l = list(map(int, input().split()))
print('-1' if sum(l) > n else n - sum(l))
