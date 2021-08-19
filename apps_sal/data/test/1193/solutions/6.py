(n, k) = map(int, input().split())
a = list(reversed(sorted(list(map(int, input().split())))))
print(a[k - 1])
