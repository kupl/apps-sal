from operator import itemgetter

n, m = map(int, input().split())
yp = []
for i in range(m):
  p_, y_ = map(int, input().split())
  yp.append([y_, p_, i+1])
py = sorted(yp)
ken = [0]*n
res = []
for i in range(m):
  ken[py[i][1]-1] += 1
  p, q, r = py[i][1], ken[py[i][1]-1], py[i][2]
  res.append([p, q, r])
#print(yp)
#print(py)

res.sort(key=itemgetter(2))
#print(res)
for i in range(m):
  ans1 = [0]*(6-len(str(res[i][0])))
  ans1.append(res[i][0])
  ans2 = [0]*(6-len(str(res[i][1])))
  ans2.append(res[i][1])
  print(*ans1, *ans2, sep='')
