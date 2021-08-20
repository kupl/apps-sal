class SparseTable:
    """区間取得クエリをO(1)で答えるデータ構造をO(NlogN)で構築する
    query(l, r): 区間[l, r)に対するクエリに答える
    """

    def __init__(self, array, n):
        n = len(array)
        self.row_size = n.bit_length()
        self.log_table = [0] * (n + 1)
        for i in range(2, n + 1):
            self.log_table[i] = self.log_table[i // 2] + 1
        self.sparse_table = [[0] * n for _ in range(self.row_size)]
        for i in range(n):
            self.sparse_table[0][i] = array[i]
        for row in range(1, self.row_size):
            for i in range(n - (1 << row) + 1):
                self.sparse_table[row][i] = self._merge(self.sparse_table[row - 1][i], self.sparse_table[row - 1][i + (1 << row - 1)])

    def _merge(self, num1, num2):
        """クエリの内容"""
        return min(num1, num2)

    def query(self, l, r):
        """区間[l, r)に対するクエリに答える"""
        row = self.log_table[r - l]
        return self._merge(self.sparse_table[row][l], self.sparse_table[row][r - (1 << row)])


(n, m) = list(map(int, input().split()))
a = list(map(int, input().split()))
MOD = 998244353
sp = SparseTable(a, n)
to_ind = {}
for i in range(n):
    to_ind[a[i]] = i
dp = [[-1] * (n + 1) for i in range(n + 1)]


def solve(l, r):
    if dp[l][r] != -1:
        return dp[l][r]
    if l == r:
        dp[l][r] = 1
        return 1
    if r - l == 1:
        dp[l][r] = 1
        return 1
    ind = to_ind[sp.query(l, r)]
    res1 = 0
    res2 = 0
    for i in range(ind + 1, r + 1):
        res1 += solve(ind + 1, i) * solve(i, r)
        res1 %= MOD
    for i in range(l, ind + 1):
        res2 += solve(l, i) * solve(i, ind)
        res2 %= MOD
    dp[l][r] = max(res1, 1) * max(res2, 1)
    dp[l][r] %= MOD
    return dp[l][r]


print(solve(0, n) % MOD)
