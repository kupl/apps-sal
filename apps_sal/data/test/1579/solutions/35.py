def main():
    n = int(input())
    xy = [list(map(int, input().split())) for _ in [0] * n]
    ixy = [[i, x, y] for i, (x, y) in enumerate(xy)]

    class unionfind():
        # size:要素数,tree：unionfind木
        def __init__(self, size):  # self,要素数
            self.size = size
            self.tree_root = list(range(self.size))
            self.tree_depth = [1] * self.size

        # rootを探す
        def root(self, index):
            temp_list = []
            temp = self.tree_root[index]
            while index != temp:
                temp_list.append(index)
                index = temp
                temp = self.tree_root[index]
            for i in temp_list:
                self.tree_root[i] = index
            return index

        # 結合
        def unite(self, index1, index2):
            r1 = self.root(index1)
            r2 = self.root(index2)
            if r1 != r2:
                d1, d2 = self.tree_depth[r1], self.tree_depth[r2]
                if d1 <= d2:
                    self.tree_root[r1] = r2
                    self.tree_depth[r2] = max(d1 + 1, d2)
                else:
                    self.tree_root[r2] = r1
                    self.tree_depth[r1] = max(d2 + 1, d1)

        # 同じか判定
        def same(self, index1, index2):
            r1 = self.root(index1)
            r2 = self.root(index2)
            return r1 == r2

        # 連結成分の個数
        def component(self):
            return len({self.root(i) for i in range(self.size)})

    u = unionfind(n)
    ixy.sort(key=lambda x: x[1])
    for i in range(n - 1):
        if ixy[i][1] == ixy[i + 1][1]:
            u.unite(ixy[i][0], ixy[i + 1][0])
    ixy.sort(key=lambda x: x[2])
    for i in range(n - 1):
        if ixy[i][2] == ixy[i + 1][2]:
            u.unite(ixy[i][0], ixy[i + 1][0])
    tate = [set() for _ in [0] * n]
    yoko = [set() for _ in [0] * n]
    cnt = [0] * n
    for i in range(n):
        r = u.root(i)
        tate[r].add(xy[i][0])
        yoko[r].add(xy[i][1])
        cnt[r] += 1
    print(sum([len(tate[i]) * len(yoko[i]) - cnt[i] for i in range(n)]))


main()
