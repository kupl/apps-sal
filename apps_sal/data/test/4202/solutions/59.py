L, R = map(int, input().split())
 
# 例：L=3000, R=10000 で考える
# (i,j)=(3000,3001)から始まり、(3000,5018)で最小(=0)
 
# R-L>=2018 のとき、(L,L+1),...,(L,L+2018)の間で最小値0を取れる
# それ以外のとき、全探索してもO((10^3)^2)で間に合う！
if R-L >= 2018:
  print(0)
else:
  m = 2019
  for i in range(L, R):
    for j in range(i+1, R+1):
      m = min(m, i*j % 2019)
  print(m)
