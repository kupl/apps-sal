n = int(input())
a = [int(i) for i in input().split()]
dic = {}
for i in range(n):
  dic[i+1] = 0
for ai in a:
  dic[ai] += 1
cnt = 0
for di in dic:
  cnt += dic[di] * (dic[di] - 1) // 2
for i in range(n):
  print(cnt - dic[a[i]] * (dic[a[i]] - 1) // 2 + (dic[a[i]] - 2) * (dic[a[i]] - 1) // 2)
