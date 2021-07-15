class DFS:
    def __init__(self):
        self.G= []
        self.leave_tree= []

    def take_input(self):
        k = int(input())
        if(k>1):
            graph =[int(node)-1 for (node) in input().split(' ')]
            self.G = [[] for _ in range(len(graph)+1)]   
            for i in range(len(graph)):
                self.G[graph[i]].append(i+1)
            self.visited = [0]*k
            self.leave_tree = [0]*k
            for i in range(k-1,-1,-1):
                if len(self.G[i])==0:
                    self.leave_tree[i]=1
                else:
                    for j in self.G[i]:
                        self.leave_tree[i]+=self.leave_tree[j]
            self.leave_tree.sort()
            print(*self.leave_tree)
        else:
            print(k)





x = DFS()
x.take_input()

