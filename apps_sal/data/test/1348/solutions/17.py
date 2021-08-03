class RestoreGraph():
    def __init__(self, n, k, dis_values):
        self.dis_values = dis_values
        self.n = n
        self.k = k

    def generate_graph(self):
        dis_pairs = [(self.dis_values[i], i) for i in range(len(self.dis_values))]
        dis_pairs = sorted(dis_pairs)
        if dis_pairs[0][0] != 0:
            print(-1)
            return
        count = [0] * self.n
        parent = [-1] * self.n
        ind = 0
        for i in range(1, self.n):
            if dis_pairs[ind][0] != dis_pairs[i][0] - 1 or count[ind] == self.k:
                ind = ind + 1
                while(ind < i and (dis_pairs[ind][0] < dis_pairs[i][0] - 1 or count[ind] == self.k)):
                    ind += 1
                if dis_pairs[ind][0] != dis_pairs[i][0] - 1 or count[ind] == self.k:
                    print(-1)
                    return
            parent[i] = ind
            count[i] += 1
            count[ind] += 1
        print(self.n - 1)
        for i in range(1, n):
            print(dis_pairs[i][1] + 1, dis_pairs[parent[i]][1] + 1)


n, k = list(map(int, input().strip(' ').split(' ')))
arr = list(map(int, input().strip(' ').split(' ')))

graph = RestoreGraph(n, k, arr)
graph.generate_graph()
