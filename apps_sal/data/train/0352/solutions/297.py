class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        def isPredecessor(word1, word2):
            if len(word1) + 1 != len(word2):
                return False
            i, j, count = 0, 0, 0
            while i < len(word1):
                if word1[i] != word2[j]:
                    count += 1
                    j += 1
                    if count > 1:
                        return False
                    continue
                i += 1
                j += 1
            return True
        
        # build graph
        numPredecessor = [0] * len(words)
        
        graph = defaultdict(lambda: [])
        for i in range(len(words)):
            for j in range(i + 1, len(words)):
                if isPredecessor(words[i], words[j]):
                    graph[i].append(j)
                    numPredecessor[j] += 1
                elif isPredecessor(words[j], words[i]):
                    graph[j].append(i)
                    numPredecessor[i] += 1
        
        # dfs for each node without predecessor
        def dfs(node, path):
            nonlocal out
            
            path.append(node)
            out = max(out, len(path))
            for nei in graph[node]:
                dfs(nei,path)
            path.pop()
            
        
        out = 0
        for node in [i for i in range(len(words)) if not numPredecessor[i]]:
            dfs(node,[])
        return out
        
        
        

