from collections import defaultdict
n, k = map(int, input().split())
m = defaultdict(int)

for _ in range(k):
  input()
  for x in input().split():
    m[int(x)] += 1

result = 0
for i in range(1, n+1):
  if m[i] == 0:
    result += 1
print(result)
