n, k = map(int, input().split())
l = list(map(int, input().split()))
# print(l)
l = sorted(l)[:k]
print(sum(l))
