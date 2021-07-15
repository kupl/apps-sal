class Solution:
    def minMalwareSpread(self, graph: List[List[int]], initial: List[int]) -> int:
        
        
        
        table={}
        
        for i in range(len(graph)):
            table[i] = []
        for i in range(len(graph)):
            for j in range(i+1,len(graph[i])):
                if graph[i][j] ==1:
                    table[i].append(j)
                    table[j].append(i)
        
        
        print(table)
        
        def DFS(n,exclude_node):
            for connect_node in table[n]:
                if connect_node not in self.visited and connect_node != exclude_node:
                    self.visited.append(connect_node)
                    DFS(connect_node,exclude_node)
        
        res=[]
        current_max = 0
        
        
        for node in initial:
            exclude = node
            self.visited=[]
            for i in range(len(initial)):
                
                if initial[i] != exclude:
                    if initial[i] not in self.visited:
                        self.visited.append(initial[i])
                    DFS(initial[i],node)
            left = len(graph)-len(self.visited)
            if left >current_max:
                res = [node]
                current_max = left
            elif left == current_max:
                res.append(node)
            print((node,self.visited))
        
        res.sort()
        print(res)
        return res[0]

