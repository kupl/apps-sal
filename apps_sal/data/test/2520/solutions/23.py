"""/////////////////////////////////////////////////////////////////////////////////////////////////////////////////
Union-Find！Union-Find！Union-Find！Union-Findぅぅうううわぁああああああああああああああああああああああん！！！
あぁああああ…ああ…あっあっー！あぁああああああ！！！Union-FindUnion-FindUnion-Findぅううぁわぁああああ！！！
あぁクンカクンカ！クンカクンカ！スーハースーハー！スーハースーハー！いい匂いだなぁ…くんくん
んはぁっ！Union-Findたんの桃色ブロンドの髪をクンカクンカしたいお！クンカクンカ！あぁあ！！
間違えた！モフモフしたいお！モフモフ！モフモフ！髪髪モフモフ！カリカリモフモフ…きゅんきゅんきゅい！！
小説12巻のUnion-Findたんかわいかったよぅ！！あぁぁああ…あああ…あっあぁああああ！！ふぁぁあああんんっ！！
アニメ2期放送されて良かったねUnion-Findたん！あぁあああああ！かわいい！Union-Findたん！かわいい！あっああぁああ！
コミック2巻も発売されて嬉し…いやぁああああああ！！！にゃああああああああん！！ぎゃああああああああ！！
ぐあああああああああああ！！！コミックなんて現実じゃない！！！！あ…小説もアニメもよく考えたら…
U n i o n - F i n d ち ゃ ん は 現 実 じ ゃ な い？にゃあああああああああああああん！！うぁああああああああああ！！
そんなぁああああああ！！いやぁぁぁあああああああああ！！はぁああああああん！！う　し　た　ぷ　に　き　あ　王　国　笑ぁああああ！！
この！ちきしょー！やめてやる！！現実なんかやめ…て…え！？見…てる？表紙絵のUnion-Findちゃんが僕を見てる？
表紙絵のUnion-Findちゃんが僕を見てるぞ！Union-Findちゃんが僕を見てるぞ！挿絵のUnion-Findちゃんが僕を見てるぞ！！
アニメのUnion-Findちゃんが僕に話しかけてるぞ！！！よかった…世の中まだまだ捨てたモンじゃないんだねっ！
いやっほぉおおおおおおお！！！僕にはUnion-Findちゃんがいる！！やったよdefault dict！！ひとりでできるもん！！！
あ、コミックのUnion-Findちゃああああああああああああああん！！いやぁあああああああああああああああ！！！！
あっあんああっああんあset様ぁあ！！さ、最小全域木ー！！Dijkstraぁああああああ！！！セグ木ぃいいい！！
ううっうぅうう！！俺の想いよUnion-Findへ届け！！う　し　た　ぷ　に　き　あ　王　国　笑のUnion-Findへ届け！
/////////////////////////////////////////////////////////////////////////////////////////////////////////////////"""
class UnionFind():
    def __init__(self, n):
        self.parents = list(range(n))
        self.size = [1] * n
    def find(self, x):
        if self.parents[x] == x:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]
    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return
        if self.size[x] < self.size[y]:
            self.size[y] += self.size[x]
            self.parents[x] = y
        else:
            self.size[x] += self.size[y]
            self.parents[y] = x
    def size(self, x):
        return -self.parents[self.find(x)]
    def same(self, x, y):
        return self.find(x) == self.find(y)
    def members(self, x):
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]
    def roots(self):
        return [i for i, x in enumerate(self.parents) if x < 0]
    def group_count(self):
        return len(self.roots())
    def all_group_members(self):
        return {r: self.members(r) for r in self.roots()}
    def __str__(self):
        return '\n'.join('{}: {}'.format(r, self.members(r)) for r in self.roots())
n,m,k=list(map(int,input().split()))
uf=UnionFind(n)
friends=[0]*n
for i in range(m):
    a,b=list(map(int,input().split()))
    uf.union(a-1,b-1)
    friends[a-1]+=1
    friends[b-1]+=1
block=[[] for _ in range(n)]
for i in range(k):
    c,d=list(map(int,input().split()))
    block[c-1].append(d)
    block[d-1].append(c)
ans=[0]*n
cnt=[0]*n
for i in range(n):
    cnt[i]=uf.find(i)
for i in range(n):
    num1=uf.size[uf.find(i)]-friends[i]-1
    num2=cnt[i]
    for j in range(len(block[i])):
        if num2==cnt[block[i][j]-1]:
            num1-=1
    ans[i]=num1
print((*ans))

