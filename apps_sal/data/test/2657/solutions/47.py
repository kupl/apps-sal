n = int(input())
a = [int(x) for x in input().split()]
a.sort()
m = max(a) // 2
res = 0
c = max(a)
for i in range(n-1):
  if abs(m - a[i]) <= c:
    res = a[i]
    c = abs(m - a[i])
print(max(a),res)
