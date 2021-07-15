N = int(input())
l = []
for i in range(N):
  s, p = input().split()
  l.append([i+1, s, int(p)])

l = sorted(l, key=lambda x:(x[1], -x[2]))
for i in range(N):
  print(l[i][0])
