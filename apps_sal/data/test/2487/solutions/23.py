class edge:

    def __init__(self, u, v):
        self.u = u
        self.v = v

    def min(self):
        return min(self.u, self.v)

    def max(self):
        return max(self.u, self.v)


N = int(input())
edge_list = []
for i in range(N - 1):
    (u, v) = list(map(int, input().split()))
    edge_list.append(edge(u - 1, v - 1))
ver_num = int(N * (N + 1) * (N + 2) / 6)
edge_num = 0
for e in edge_list:
    edge_num += (N + 1 - (e.max() + 1)) * (e.min() + 1)
print(ver_num - edge_num)
