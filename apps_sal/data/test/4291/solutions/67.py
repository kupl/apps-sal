n, q = map(int, input().split())
s = input()
ac = {1:0}
k = 0
for i in range(1, n):
  if s[i - 1:i + 1] == 'AC':
    k += 1
  ac[i + 1] = k
ans = []
for i in range(q):
  l, r = map(int, input().split())
  ans.append(ac[r] - ac[l])
for e in ans:
  print(e)
