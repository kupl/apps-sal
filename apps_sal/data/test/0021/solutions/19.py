n = int(input())
l = list(map(int, input().split()))
idx_min = l.index(1)
idx_max = l.index(n)
arr = []
arr.append(abs(0 - idx_max))
arr.append(abs(n - 1 - idx_max))
arr.append(abs(0 - idx_min))
arr.append(abs(n - 1 - idx_min))
print(max(arr))
