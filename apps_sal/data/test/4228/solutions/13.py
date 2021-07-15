n, l = map(int, input().split())
L = []
a = 0
if 0 <= l:
  a = l
else:
  a = n - 1 + l
for i in range(n):
  if (l + i) == 0:
    a = 0
  L.append(l + i)
L.remove(a)
print(sum(L))
