n, k = map(int, input().split())

trees = []
for _i in range(n):
  tree = int(input())
  trees.append(tree)

trees.sort()
ans = float('inf')

for i in range(n - k + 1):
  diff = trees[i + k - 1] - trees[i]
  if ans > diff:
    ans = diff

print(ans)
