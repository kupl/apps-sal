n = int(input())
a = list(map(int, input().split()))
print(a.index(max(a)) + 1, max(a[:a.index(max(a))] + a[a.index(max(a)) + 1:]))
