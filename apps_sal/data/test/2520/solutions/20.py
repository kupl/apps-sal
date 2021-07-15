class UnionFind():
    def __init__(self, n):	#初期化
        self.n = n
        self.parents = [-1] * n
    def find(self, x):		#属すグループの根(リーダー)
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]
    def union(self, x, y):	#連結
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return
        if self.parents[x] > self.parents[y]:
            x, y = y, x
        self.parents[x] += self.parents[y]
        self.parents[y] = x
    def size(self, x):		#同じグループに属す頂点数
        return -self.parents[self.find(x)]
    def same(self, x, y):	#x,yが同じグループに属しているかどうか
        return self.find(x) == self.find(y)
    def members(self, x):	#同じグループに属すメンバー
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]
    def roots(self):		#全ての根(リーダー)
        return [i for i, x in enumerate(self.parents) if x < 0]
    def group_count(self):	#グループの数
        return len(self.roots())
    def all_group_members(self):#全てのグループのメンバー
        return {r: self.members(r) for r in self.roots()}
    def __str__(self):		#根：{所属しているメンバー}
        return '\n'.join('{}: {}'.format(r, self.members(r)) for r in self.roots())


n,m,k = map(int,input().split())
suggest = UnionFind(n)
follow = [0]*n
block = [0]*n
for i in range(n):
    follow[i] = list()
    block[i]  = list()
for _ in range(m):
    a,b = map(int,input().split())
    a -= 1
    b -= 1
    suggest.union(a,b)
    follow[a].append(b)
    follow[b].append(a)

for _ in range(k):
    c,d = map(int,input().split())
    c -= 1
    d -= 1
    block[c].append(d)
    block[d].append(c)
ans = ""
suggestfriend = [0]*n
ans = ""
for i in range(n):
    blockperson = 0
    union = suggest.size(i)
    for j in range(len(block[i])):
        if(suggest.same(i,block[i][j])):
            blockperson += 1
    ans += str(union - blockperson -len(follow[i]) - 1) + " "
print(ans)
