class Solution:
    
    
    def isChild(self, parent, possible_child):
        for i in range(len(possible_child)):
            if possible_child[:i] + possible_child[i+1:] == parent:
                return True 
        return False
    
    def longestStrChain(self, words: List[str]) -> int:
        
        # an intutitve idea is to create a graph of the given words, where every node is a word, and is a predecessor to all of its children. We can then simply DFS from root to node and find the longest path.
        # the DFS would take O(n) where n is the length of words.
        # Challenge: how to construct graph? We can loop once and bucket words by their length, and create a node per word, then starting from the smallest word length i, find all possible children of length i+1 and add them as edges do this until the end. 
        # bucketing and creating graph nodes would take O(n), connecting nodes would also take o(n) since we only check two buckets at a time linearly, and those buckets at most contain n nodes (and in that case other buckets are empty), so its O(n)
        
        
        graph = {}
        # word length buckets 
        word_lens = [[] for _ in range(17)]
        # create nodes and bucket
        for w in words:
            graph[w] = []
            word_lens[len(w)].append(w)
        
        # connect graph
        for i in range(1,16):
            parents = word_lens[i]
            possible_children = word_lens[i+1]
            for p in parents: 
                for c in possible_children:
                    # check if c can possibly be a child of p
                    # it is a possible child if 
                    if self.isChild(p,c):
                        graph[p].append(c)
       # do DFS 
        longest_len = 0
        for node in graph.keys():
            to_visit = [(node,1)]
            
            while(len(to_visit) != 0):
                cur_node,depth = to_visit.pop()
                longest_len = max(depth, longest_len)
                for child in graph[cur_node]: 
                    to_visit.append((child,depth+1))
            
        return longest_len
