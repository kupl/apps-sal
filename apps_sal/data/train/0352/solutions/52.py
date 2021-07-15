from collections import defaultdict
from queue import Queue

class Solution:
    def is_pred(self, w1, w2):
        for i in range(len(w2)):
            if w2[:i] + w2[i+1:] == w1:
                return True
        return False
            
    def longestStrChain(self, words: List[str]) -> int:
        graph = defaultdict(list)
        words_by_len = defaultdict(list)
        for word in words:
            n = len(word)
            words_by_len[n].append(word)
        
        roots = set(words)
        for word in words:
            possible_preds = words_by_len[len(word)-1]
            for pred in possible_preds:
                if self.is_pred(pred, word):
                    graph[pred].append(word)
                    if word in roots:
                        roots.remove(word)
        
        max_depth = 1
        for root in roots:
            q = Queue()
            q.put((root, 1))
            while not q.empty():
                curr, depth = q.get()
                max_depth = max(max_depth, depth)
                descs = graph[curr]
                for desc in descs:
                    q.put((desc, depth+1))
        return max_depth
            
            
            

