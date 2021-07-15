n, l =list(map(int, input().split()))
arr = []
arr2 = []
for k in range(1, n+1):
  arr.append(abs(l + k - 1))
for k in range(1, n+1):
  arr2.append(l + k - 1)
arr2.pop(arr.index(min(arr)))
print(sum(arr2))
