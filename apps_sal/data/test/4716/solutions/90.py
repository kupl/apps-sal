(n, k) = map(int, input().split())
l = sorted(list(map(int, input().split())))[::-1]
print(sum(l[:k]))
