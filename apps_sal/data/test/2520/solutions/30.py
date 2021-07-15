#これを求めるには

#（頂点iの連結サイズ）　ー　（頂点iと頂点jが同じ連結成分に含まれて人iと人jが友達関係もしくはブロック関係にあるjの数）ー　１

#を計算すれば良い


class UnionFind():
    def __init__(self,N):
        self.parents = [-1]*N

    def root(self,x):
        if self.parents[x] < 0:
            return x
        else:
            return self.root(self.parents[x])
    
    def unite(self,x,y):
        x,y = self.root(x), self.root(y)
        if x == y:
            return 
        else:
            if x > y:
                x,y = y,x
            self.parents[x] += self.parents[y]
            self.parents[y] = x
            return


N,M,K = list(map(int,input().split()))
AB = [list(map(int,input().split())) for _ in range(M)]
CD = [list(map(int,input().split())) for _ in range(K)]

u = UnionFind(N)
f = [set() for _ in range(N)]
#要素数がN個の集合の配列　f = [{},{},{},...,{}]

l = [set() for _ in range(N)]
#上記と同様

for a,b in AB:
    a,b = a-1,b-1
    #配列の最初（a = 0,b = 0）から開始するため

    f[a].add(b)
    #f = [...,{b},{},...,{}]
    #配列のa番目の集合の要素にbを加える

    f[b].add(a)
    #f = [.....,{a},{}..,{}]
    #配列のb番目の集合の要素にaを加える

    u.unite(a,b)


for c,d in CD:
    c,d = c-1,d-1
    l[c].add(d)
    l[d].add(c)

ans = [0] * N
#ブロック関係は同じ連結成分かどうかで引くか変わってくる
#同じ連結成分にあるならば、全体の連結成分のサイズから引く
for i in range(N):
    r = u.root(i)
    bl = 0
    #「bl」は引くべきブロック関係の数
    for j in l[i]:
        if u.root(j) == r:
            bl += 1
    
    ans[i] = -u.parents[r] - len(f[i]) - bl -1
print((' '.join(list(map(str,ans)))))


