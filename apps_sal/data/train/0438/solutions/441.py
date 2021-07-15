
class Node:
    def __init__(self, parent, value):
        self.value = value
        self.parent = parent
        self.size = 1
        self.rank = 0

class UnionFind:
    def __init__(self, nodes):
        self.subsets = [Node(i, v) for i, v in enumerate(nodes)]
        self.maxSubSetSize = 1

    def union(self, i, j):
        irep = self.find(i)
        jrep = self.find(j)
        if irep == jrep:
            return
        if self.subsets[irep].rank > self.subsets[jrep].rank:
            self.subsets[jrep].parent = irep
            self.subsets[irep].size += self.subsets[jrep].size
            self.maxSubSetSize = max(self.maxSubSetSize, self.subsets[irep].size)
        else:
            self.subsets[irep].parent = jrep
            self.subsets[jrep].size += self.subsets[irep].size
            if self.subsets[irep].rank == self.subsets[jrep].rank:
                self.subsets[jrep].rank += 1
            self.maxSubSetSize = max(self.maxSubSetSize, self.subsets[jrep].size)
    
    def find(self, index):
        if self.subsets[index].parent != index:
            self.subsets[index].parent = self.find(self.subsets[index].parent)
        return self.subsets[index].parent
        

class Solution:
    def findLatestStep(self, arr: List[int], m: int) -> int:
        arr0 = [a - 1 for a in arr]
        uf = UnionFind(list(range(len(arr0))))
        lengthMSets = set()
        last_step = -1
        if m == 1:
            lengthMSets.add(arr0[0])
            last_step = 1
        visited = [False for _ in arr0]
        visited[arr0[0]] = True
        for i in range(1, len(arr0), 1):
            num = arr0[i]
            visited[num] = True
            if  num - 1 >= 0 and visited[num-1]:
                left_rep = uf.find(num-1)
                if left_rep in lengthMSets:
                    lengthMSets.remove(left_rep)
                uf.union(left_rep, num)
            if num + 1 < len(visited)and  visited[num+1]:
                right_rep = uf.find(num+1)
                if right_rep in lengthMSets:
                    lengthMSets.remove(right_rep)
                uf.union(right_rep, num)
            if uf.subsets[uf.find(num)].size == m:
                lengthMSets.add(uf.find(num))
            if len(lengthMSets) > 0:
                last_step = i + 1
        return last_step

