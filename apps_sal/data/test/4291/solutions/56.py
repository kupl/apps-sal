import bisect
n,q = map(int, input().split(" "))
s = input()
lr = [list(map(int, input().split(" "))) for i in range(q)]
a = []
for i in range(n-1):
  if s[i] +s[i+1]== 'AC':
    a.append(i+1)
for l, r in lr:
  print(bisect.bisect(a, r-1) - bisect.bisect(a, l-0.1))
