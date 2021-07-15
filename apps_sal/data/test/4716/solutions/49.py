n, k = list(map(int, input().split()))
l = sorted(list(map(int, input().split())), reverse=True)
res = l[:k]
print((sum(res)))

