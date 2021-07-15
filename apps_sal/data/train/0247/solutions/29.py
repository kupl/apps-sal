class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        n = len(arr)
        acc = dict()
        acc[-1] = 0
        for i in range(0, n):
            acc[i] = acc[i-1] + arr[i]
        best_to = [n + 1 for _ in range(n)]
        best_from = dict()
        min_total = n + 1 # Naturally impossible length. Will be updated if any possible case exist. Will tell when no possible case
        min_left = n + 1
        sum_left = 0
        s_left = 0
        
        for i in range(n):
            sum_left = acc[i] - acc[s_left-1]
            # if i == 3:
                # print(s_left)
                # print(sum_left)
            if sum_left == target:
                best_to[i] = i - s_left + 1
                best_from[s_left] = i - s_left + 1
            elif sum_left > target:
                while s_left < i:
                    s_left += 1
                    if acc[i] - acc[s_left-1] < target:
                        break
                    if acc[i] - acc[s_left-1] == target:
                        best_to[i] = i - s_left + 1
                        best_from[s_left] = i - s_left + 1
                        break
        
        for i in range(1, n):
            best_to[i] = min(best_to[i], best_to[i-1])
            
        # print(best_to)
        # print(best_from)
        
        for i in range(n - 1):
            if best_to[i] > n:
                continue
            
            if i + 1 in best_from:
                min_total = min(min_total, best_to[i] + best_from[i + 1])
        
        if min_total > n:
            return -1
        
        return min_total

