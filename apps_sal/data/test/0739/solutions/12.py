class Matrix:

  def __init__(self, mat, mod=10**9+7):
    assert(len(mat) and len(mat[0]))
    from copy import deepcopy
    self.MOD = mod
    self.mat = deepcopy(mat)

  def matunit(self, n):
    return Matrix([[(x==y) for x in range(n)] for y in range(n)], mod=self.MOD)

  def __add__(self, other):
    assert(len(self.mat)==len(other.mat) and len(self.mat[0])==len(other.mat[0]))
    h = len(self.mat)
    w = len(self.mat[0])
    ret = [[(self.mat[y][x]+other.mat[y][x])%self.MOD for x in range(w)] for y in range(h)]
    return ret

  def __mul__(self, other):
    assert(len(self.mat[0])==len(other.mat))
    h = len(self.mat)
    w = len(other.mat[0])
    ret = [[0 for _ in range(w)] for _ in range(h)]
    for y in range(h):
      for z in range(len(other.mat)):
        for x in range(w):
          ret[y][x] += self.mat[y][z]*other.mat[z][x]
    for y in range(h):
      for x in range(w):
        ret[y][x] %= self.MOD
    return Matrix(ret, mod=self.MOD)

  def __pow__(self, k):
    assert(len(self.mat)==len(self.mat[0]))
    from copy import deepcopy
    ret = self.matunit(len(self.mat))
    n = Matrix(deepcopy(self.mat), mod=self.MOD)
    while k:
      if k&1:
        ret = ret * n
      n = n * n
      k >>= 1
    return ret

  def __str__(self):
    return "[{}]".format("\n".join(str(row) for row in self.mat))

L, A, B, M = list(map(int, input().split()))

d = [0 for i in range(20)]
for i in range(1, 19):
  l = -1
  r = L
  while r-l>1:
    m = (l+r)//2
    if len(str(A+B*m))>i:
      r = m
    else:
      l = m
  d[i] = r

x = Matrix([[0, A, 1]], mod=M)
for i in range(1, 19):
  dt = d[i]-d[i-1]
  y = Matrix([[10**i, 0, 0], [1, 1, 0], [0, B, 1]], mod=M)
  y = y ** dt
  x *= y
print((x.mat[0][0]))

