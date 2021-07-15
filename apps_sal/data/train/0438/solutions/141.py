class Solution:
    def findLatestStep(self, arr: List[int], m: int) -> int:
        n = len(arr)
        arr.append(n+1)
        start = {}
        finish = {}
        last = -1
        for level,i in enumerate(arr):
            if i-1 not in finish: finish[i-1] = i 
            if i+1 not in start: start[i+1] = i

            s, f = finish[i-1], start[i+1]
            start[s] = f 
            finish[f] = s
            
            for os, of in [[i+1, start[i+1]], [finish[i-1], i-1]]:
                if of-os+1 == m: last = level
                
            del start[i+1]
            del finish[i-1]
            
        return last
