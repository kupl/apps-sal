n, m = list(map(int, input().split()))
arr = [input() for _ in range(n)]
set1 = []
set2 = []
for i in range(n):
  for j in range(m):
    if arr[i][j]=='S':
      set1.append(i)
      set2.append(j)
len1 = int(n - len(set(set1)))
len2 = int(m - len(set(set2)))

print(len1 * m + len2 *n - len2 * len1)



