from collections import Counter

class Solution:
    def maxLength(self, arr: List[str]) -> int:
        self.max_len = 0
        for i, s in enumerate(arr):
            self.bfs(Counter(s), arr, i)
        return self.max_len
    
    def bfs(self, counter, arr, _index):
        if max(counter.values()) > 1: return
        if len(counter) > self.max_len:
            self.max_len = len(counter)
        
        for i in range(_index + 1, len(arr)):
            s = arr[i]
            counter_copy = copy.copy(counter)
            counter_copy.update(Counter(s))
            self.bfs(counter_copy, arr, i)

