class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        smallest = [math.inf] * len(arr) 
        q = deque()
        curr_sum = 0
        result = math.inf
        for i, n in enumerate(arr):
            curr_sum += n
            q.append(i)
            while curr_sum > target:
                curr_sum -= arr[q.popleft()]
            
            if curr_sum == target:
                if i == 0:
                    smallest[i] = len(q)
                else:
                    smallest[i] = min(len(q), smallest[i-1])
                    # if q[0] > 0:
                    result = min(result, smallest[q[0]-1] + len(q))
            else:
                # if i > 0:
                smallest[i] = smallest[i-1]
        return -1 if result == math.inf else result
