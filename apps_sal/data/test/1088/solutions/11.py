class union_find:
  def __init__(self, n):
    self.par = [-1] * n

  def find(self, x):#xの親を見つける
    if self.par[x] < 0:
      return x
    else:
      self.par[x] = self.find(self.par[x])
      return self.par[x]

  def unite(self,x,y):#要素xとｙを併合させる
    x,y=self.find(x),self.find(y)#xとyの親の検索
    if x!=y:#親が異なる場合併合させる
      if x>y:
        x,y=y,x#小さい方をxとする. これにより要素の値が小さいものを優先して木の根とする. 
      self.par[x]+=self.par[y] #値を無向木の要素数の和にする.
      self.par[y]=x #枝側は根の位置を格納

  def same(self, x, y):#要素xと要素yが同じ無向木に所属しているかを判定する
    return self.find(x) == self.find(y)#同じ値を持つか否か

  def size(self, x):#要素xが所属する無向木の大きさを返す
    return-self.par[self.find(x)] 

import itertools  
mod = 998244353
def main():
  n, k = map(int,input().split())
  factorial = [1]
  for i in range(1, n+1):
    factorial.append(factorial[i-1]*i%mod)
  a = []
  for i in range(n):
    a.append(list(map(int, input().split())))
  gyou = union_find(n)
  for x, y in itertools.combinations(range(n), 2):
    flag = True
    for i in range(n):
      if a[x][i] + a[y][i] > k:
        flag = False
        break
    if flag:
      gyou.unite(x, y)
  retu = union_find(n)
  
  for x, y in itertools.combinations(range(n), 2):
    flag = True
    for i in range(n):
      if a[i][x] + a[i][y] > k:
        flag = False
        break
    if flag:
      retu.unite(x, y)
  ans = 1
  for i in range(len(retu.par)):
    if retu.par[i] < 0:
      ans *=factorial[-retu.par[i]]
    ans %= mod
  for i in range(len(gyou.par)):
    if gyou.par[i] < 0:
      ans *= factorial[-gyou.par[i]]
    ans %= mod
  print(ans)  
  
def __starting_point():
  main()
__starting_point()
