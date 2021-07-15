n, k = [int(i) for i in input().split()]
r, s, p = [int(i) for i in input().split()]
t = list(input())
ans = 0
dic = {'p': s, 's': r, 'r': p}
for i in range(k):
  ans += dic[t[i]]
dic_ls = []
for i in range(k, n):
  if t[i] != t[i - k]:
    ans += dic[t[i]]
  else:
    t[i] = 'j'
print(ans)
