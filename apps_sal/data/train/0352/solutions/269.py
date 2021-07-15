from collections import deque

class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        
        # return self.run_graph_solution(words)
        return self.run_dp_solution(words)
    
    def run_dp_solution(self, words):
        
        mem = {'': 0}
        
        def inner(w):
            if w in mem or w not in words:
                return
            
            max_per_w = 1
            for j in range(len(w)):
                cur = w[:j] + w[j+1:]
                if cur in mem:
                    val = mem[cur] + 1
                else:
                    inner(cur)
                    if cur not in mem:
                        val = 1
                    else:
                        val = mem[cur] + 1
                if val > max_per_w:
                    max_per_w = val
            mem[w] = max_per_w
            return
        
        for w in words:
            inner(w)
            
        return max(mem.values())
        
    def run_graph_solution(self, words):
        graph = {word: [] for word in words}
        lengths = {k: [] for k in range(1, 17)}
        into = {}
        min_len = 17
        max_len = 1
        for word in words:
            lengths[len(word)].append(word)
            min_len = min(len(word), min_len)
            max_len = max(len(word), max_len)
                    
        for k in range(min_len, max_len):
            for word1 in lengths[k]:
                for word2 in lengths[k + 1]:
                    for i in range(len(word2)):
                        if word2[:i] + word2[i+1:] == word1:
                            graph[word1].append(word2)
                            into[word2] = True     
                            
        sources = [word for word in words if word not in into]
        max_len = 0
        for s in sources:
            max_len = max(max_len, self.run_bfs(s, graph))
        return max_len
                
    def run_bfs(self, s, graph):
        queue = deque(maxlen=len(list(graph.keys())))
        queue.appendleft((s, 1))
        summary = []
        
        while len(queue) > 0:
            current_node, cur_len = queue.pop()
            for word in graph[current_node]:
                queue.appendleft((word, cur_len + 1))
            summary.append(cur_len)
        
        return summary[-1]
    
    
            
            
        
        
        
        
        

