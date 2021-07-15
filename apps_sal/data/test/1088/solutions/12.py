class dsu():
    """Data structures and algorithms for disjoint set union problems.
    
    Given an undirected graph, it processes the following queries in O(alpha(n)) time (amortized).

    >   Edge addition
    
    >   Deciding whether given two vertices are in the same connected component

    Each connected component internally has a representative vertex.

    When two connected components are merged by edge addition, one of the two representatives of these connected components becomes the representative of the new connected component.
    """


    __slots__ = ["_n", "parent_or_size"]


    def __init__(self, n):
        """
        It creates an undirected graph with n vertices and 0 edges.
        
        Constraints
        -----------

        >   0 <= n <= 10 ** 8

        Complexity
        ----------

        >   O(n)
        """
        self._n = n
        self.parent_or_size = [-1] * n
    
    
    def merge(self, a, b):
        """
        It adds an edge (a, b).

        If the vertices a and b were in the same connected component, it returns the representative of this connected component. Otherwise, it returns the representative of the new connected component.
       
        Constraints
        -----------

        >   0 <= a < n 

        >   0 <= b < n
        
        Complexity
        ----------

        >   O(alpha(n)) amortized
        """
        # assert 0 <= a < self._n
        # assert 0 <= b < self._n
        x = self.leader(a)
        y = self.leader(b)
        if x == y:
            return x
        else:
            if self.parent_or_size[y] < self.parent_or_size[x]:
                x, y = y, x
            self.parent_or_size[x] += self.parent_or_size[y]
            self.parent_or_size[y] = x


    def same(self, a, b):
        """
        It returns whether the vertices a and b are in the same connected component.

        Constraints
        -----------

        >   0 <= a < n

        >   0 <= b < n

        Complexity
        ----------

        >   O(alpha(n)) amortized
        """
        # assert 0 <= a < self._n
        # assert 0 <= b < self._n
        return self.leader(a) == self.leader(b)


    def leader(self, a):
        """
        It returns the representative of the connected component that contains the vertex a.

        Constraints
        -----------

        >   0 <= a < n

        Complexity
        ----------

        >   O(alpha(n)) amortized
        """
        # assert 0 <= a < self._n
        path = []
        while self.parent_or_size[a] >= 0:
            path.append(a)
            a = self.parent_or_size[a]
        for child in path:
            self.parent_or_size[child] = a
        return a

    
    def size(self, a):
        """
        It returns the size of the connected component that contains the vertex aa.

        Constraints
        -----------

        >   0 <= a < n
        
        Complexity
        ----------

        >   O(alpha(n)) amortized
        """
        # assert 0 <= a < self._n
        return -self.parent_or_size[self.leader(a)]


    def groups(self):
        """
        It divides the graph into connected components and returns the list of them.

        More precisely, it returns the list of the "list of the vertices in a connected component". Both of the orders of the connected components and the vertices are undefined.

        Complexity
        ----------

        >   O(n)
        """
        result = [[] for _ in range(self._n)]
        for i in range(self._n):
            result[self.leader(i)].append(i)
        return [g for g in result if g]



MOD = 998244353
table_len = 110

fac = [1, 1]
for i in range(2, table_len):
    fac.append(fac[-1] * i % MOD)

finv = [0] * table_len
finv[-1] = pow(fac[-1], MOD - 2, MOD)
for i in range(table_len-1, 0, -1):
    finv[i-1] = finv[i] * i % MOD

N, K = list(map(int, input().split()))
As = [list(map(int, input().split())) for _ in range(N)]

def solve_row(mat):
    uf = dsu(N)
    for i in range(N):
        for j in range(i + 1, N):
            for k in range(N):
                if mat[i][k] + mat[j][k] > K:
                    break
            else:
                uf.merge(i, j)
    groups = uf.groups()
    ret = 1
    for g in groups:
        ret *= fac[len(g)]
        ret %= MOD
    return ret

tAs = list(map(list, list(zip(*As))))
print((solve_row(As) * solve_row(tAs) % MOD))


