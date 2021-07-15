class UnionFind:
    def __init__(self, n: int) -> None:
        #マイナスならルートでその深さを表す。プラスならルートのノードを指す。
        self.nodes = [-1]*n
 
    def find_root(self, x: int) -> int:
        if self.nodes[x] < 0:
            return x
        else:
            self.nodes[x] = self.find_root(self.nodes[x])
            return self.nodes[x]
 
    def unite(self, x: int, y: int) -> None:
        x, y = self.find_root(x), self.find_root(y)
        #浅い方につなぐ
        if (x != y):
            if (x < y):
                self.nodes[y] += self.nodes[x]
                self.nodes[x] = y
            else:
                self.nodes[x] += self.nodes[y]
                self.nodes[y] = x
                
    def get_num(self, x: int) -> int:
        return -(self.nodes[x])

MAX = 10**5+1

N = int(input())
uf = UnionFind(2*MAX)

for i in range(N):
  x,y = list(map(int, input().split()))
  uf.unite(x,y+MAX)

#数え上げ
num_x = [0]*2*MAX
num_y = [0]*2*MAX
for i in range(MAX):
  num_x[uf.find_root(i)] += 1
  num_y[uf.find_root(i+MAX)] += 1
  #print(num_x[uf.find_root(i)], num_y[uf.find_root(i+MAX)])

ans = 0
for i in range(2*MAX):
  ans += num_x[i] * num_y[i]

print((ans - N))

