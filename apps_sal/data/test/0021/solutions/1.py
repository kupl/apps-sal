n = int(input())
a = list(map(int, input().split()))
i, j = sorted([a.index(1), a.index(n)])
print(max(j, n - i - 1))
