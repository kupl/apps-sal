(n, k) = map(int, input().split())
a = sorted(list(map(int, input().split())))[::-1]
print(sum(a[k:]))
