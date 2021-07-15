from collections import defaultdict
b = defaultdict(int)
c = defaultdict(int)
n = int(input())
a = map(int, input().split())

for idx,i in enumerate(a, start=1):
  b[i - idx] += 1
  c[i + idx] += 1
ans = 0
for k,v in b.items():
  ans += (v * c[-1 * k])
print(ans)
