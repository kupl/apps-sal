N = int(input())
l = []
for i in range(N):
  s, p = input().split()
  l.append([s, -int(p), i+1])

# 地名に関して辞書順に / (-点数)に関して昇順に（点数に関して降順に）並べる
l = sorted(l, key=lambda x:(x[0], x[1]))
for i in range(N):
  print(l[i][2])
