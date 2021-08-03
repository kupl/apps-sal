class Solution:
    def largestComponentSize(self, A: List[int]) -> int:
        d = {}
        for i in range(len(A)):
            for j in range(2, int(math.sqrt(A[i]) + 1)):
                if A[i] % j == 0:
                    if j not in d:
                        d[j] = []
                    if A[i] // j not in d:
                        d[A[i] // j] = []
                    d[j].append(i)
                    d[A[i] // j].append(i)
            if A[i] not in d:
                d[A[i]] = []
            d[A[i]].append(i)

        self.father = list(range(len(A)))
        for k, v in list(d.items()):
            if len(v) > 1:
                for i in range(len(v) - 1):
                    self.union(v[i], v[i + 1])
        for i in range(len(self.father)):
            self.find(i)
        return Counter(self.father).most_common()[0][1]

    def find(self, x):
        if self.father[x] == x:
            return x
        else:
            self.father[x] = self.find(self.father[x])
            return self.father[x]

    def union(self, x, y):
        x_father = self.find(x)
        y_father = self.find(y)
        if x_father != y_father:
            self.father[x_father] = y_father
