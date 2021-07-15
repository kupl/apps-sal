import numpy as np
class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        cumsum = np.cumsum(arr)
        h2idx = {}
        
        print(cumsum)
        minSum = []
        for idx,c in enumerate(cumsum):
            # print(c, target, target-c, h2idx)
            if c == target: 
                minSum.append(idx+1)
            if (c - target) in h2idx:
                minSum.append(idx - h2idx[c - target])
            h2idx[c] = idx
        if len(minSum) < 2: return -1
        return sum(list(sorted(minSum))[:2])
            
# t = 7
# [ 2, 2, 3, 4, 3, 4]

    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        prefix = {0: -1}
        best_till = [math.inf] * len(arr)
        ans = best = math.inf
        for i, curr in enumerate(itertools.accumulate(arr)):
            if curr - target in prefix:
                end = prefix[curr - target]
                if end > -1:
                    ans = min(ans, i - end + best_till[end])
                best = min(best, i - end)
            best_till[i] = best
            prefix[curr] = i
        return -1 if ans == math.inf else ans
    
    
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        cumsum = np.cumsum(arr)
        h2idx = {}
        INF = math.inf
        print(cumsum)
        best_at_i = [INF] * len(arr)
        best = INF
        for idx,c in enumerate(cumsum):
            # print(c, target, target-c, h2idx)
            if c == target: 
                # print('sdfjsldfjksdl')
                # best = min(best, best_at_i[left-1] + idx+1)
                best_at_i[idx] = min(best_at_i[idx-1], idx+1)
            if (c-target) in h2idx:
                # print('fhgjdkg')
                left = h2idx[c-target]
                best = min(best, best_at_i[left] + idx - left)
                best_at_i[idx] = min(best_at_i[left], idx - left)
                # print(idx, left, best_at_i[left], best)
            h2idx[c] = idx
            best_at_i[idx] = min(best_at_i[idx-1], best_at_i[idx])
            
        print(best_at_i, h2idx)
        return best if best != INF else -1
