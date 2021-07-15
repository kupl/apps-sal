n, k = map(int, input().split())
l = list(map(int, input().split()))
l_sort = sorted(l)
print(sum(l_sort[-k:]))
