n = int(input())
l = list(map(int, input().split()))

count = 0
for i in range(n - 2):
  for j in range(i + 1, n - 1):
    for k in range(j + 1, n):
      if (l[i] + l[j] > l[k]) and (l[j] + l[k] > l[i]) and (l[i] + l[k] > l[j]) and (l[i] != l[j]) and (l[j] != l[k]) and (l[i] != l[k]):
        count += 1
print(count)

