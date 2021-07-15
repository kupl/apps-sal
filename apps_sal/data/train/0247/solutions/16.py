class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        prefix = {0:-1}
        best_sofar_arr = [math.inf]
        best_sofar = math.inf
        curr_best = math.inf
        ans = math.inf
        new_ans = math.inf
        for i, curr in enumerate(itertools.accumulate(arr)):
            prefix[curr] = i
            if curr - target in prefix:
                curr_best = (i-prefix[curr - target]) 
                best_sofar = min(best_sofar, curr_best)
                best_sofar_arr.append(best_sofar)
                if i > 0 :
                    new_ans = curr_best + best_sofar_arr[prefix[curr - target]+1]
                ans = min(new_ans, ans)            
            else:
                best_sofar_arr.append(best_sofar)
        return -1 if ans==math.inf else ans
