from operator import itemgetter


class SegmentTree():
    """一点更新、区間取得クエリをそれぞれO(logN)で答えるデータ構造を構築する
    update: i番目をvalに変更する
    get_min: 区間[begin, end)の最小値を求める
    """

    def __init__(self, n):
        self.n = n
        self.INF = 10**18
        self.size = 1
        while self.size < n:
            self.size *= 2
        self.node = [self.INF] * (2 * self.size - 1)

    def update(self, i, val):
        i += (self.size - 1)
        self.node[i] = val
        while i > 0:
            i = (i - 1) // 2
            self.node[i] = min(self.node[2 * i + 1], self.node[2 * i + 2])

    def get_min(self, begin, end):
        begin += (self.size - 1)
        end += (self.size - 1)
        s = self.INF
        while begin < end:
            if (end - 1) & 1:
                end -= 1
                s = min(s, self.node[end])
            if (begin - 1) & 1:
                s = min(s, self.node[begin])
                begin += 1
            begin = (begin - 1) // 2
            end = (end - 1) // 2
        return s


n, k = map(int, input().split())
s = input()
info = []
for i, char in enumerate(s):
    if char == "0":
        info.append((i, i + 1, i + 1))
    else:
        info.append((max(i - k, 0), min(i + k + 1, n), i + 1))
info = sorted(info, key=itemgetter(1))

st = SegmentTree(n + 1)
for begin, end, cost in info:
    if begin == 0:
        tmp = min(st.get_min(end - 1, end), cost)
    else:
        tmp = min(st.get_min(end - 1, end), st.get_min(begin - 1, end) + cost)
    st.update(end - 1, tmp)
print(st.get_min(end - 1, end))
