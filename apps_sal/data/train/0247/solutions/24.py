class Solution:
  # 864 ms
  def minSumOfLengths(self, arr, target):
    result = inf = 2**31-1
    i = window = count = 0
    # preMin: store previous shortest length
    preMin = deque([(-1, inf)])

    # i: window start, j: window end
    for j, num in enumerate(arr):
      window += num
      while window > target:
        window -= arr[i]
        i += 1
        
      while len(preMin) >= 2 and preMin[1][0] <= i-1:
        preMin.popleft()
      
      if window == target:
        # curr: current length
        curr = j - i + 1

        # find first minimal length n before window start i
        n = preMin[0][1]
        # update result if less    
        if result > curr + n: result = curr + n
            
        # update shortest length if less
        if curr < preMin[-1][-1]: preMin.append((j, curr))
          
        # early stopping if found two single targets
        if curr == 1: count += 1
        if count == 2: return 2

    return result if result < inf else -1
