class Solution:

    def longestSubarray(self, nums: List[int], limit: int) -> int:
        n = len(nums)
        max_q = deque() #3,2,1,0
        min_q = deque() #1,2,3,4

        start = 0
        ans = 0
        for end in range(n):
            while max_q and max_q[-1] < nums[end]:
                max_q.pop()
            while min_q and min_q[-1] > nums[end]:
                min_q.pop()
            max_q.append(nums[end])
            min_q.append(nums[end])
            
            if max_q[0] - min_q[0] > limit:
                if max_q[0] == nums[start]:
                    max_q.popleft()
                
                if min_q[0] == nums[start]:
                    min_q.popleft()
                
                start += 1
            
            ans = max(end-start+1, ans)
        return ans

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    def longestSubarray2(self, nums: List[int], limit: int) -> int:
        #[10,1,2,4,7,2]
        #queue = [4, 7, 2, 8]
        #min_queue = [2, 8]
        #max_queue = [8]
        #limit: 5
        #ans: 4
        q = deque()
        min_q = deque()
        max_q = deque()
        ans = 0
        for num in nums:
            q.append(num)
            while min_q and min_q[-1] > num:
                min_q.pop()
            min_q.append(num)
            while max_q and max_q[-1] < num:
                max_q.pop()
            max_q.append(num)
            while q and max_q[0] - min_q[0] > limit:
                del_num = q.popleft()
                if max_q[0] == del_num:
                    max_q.popleft()
                if min_q[0] == del_num:
                    min_q.popleft()
            ans = max(ans, len(q))
        return ans

    def longestSubarray2(self, nums: List[int], limit: int) -> int:
        #[10,1,2,4,7,2]
        #queue = [4, 7, 2, 8]
        #min_queue = [2, 8]
        #max_queue = [8]
        #limit: 5
        #ans: 4

        min_q = deque()
        max_q = deque()
        start = 0
        for num in nums:
            while min_q and min_q[-1] > num:
                min_q.pop()
            min_q.append(num)

            while max_q and max_q[-1] < num:
                max_q.pop()
            max_q.append(num)

            if max_q[0] - min_q[0] > limit:
                if max_q[0] == nums[start]:
                    max_q.popleft()
                if min_q[0] == nums[start]:
                    min_q.popleft()
                start += 1
        return len(nums) - start

        
        

    def longestSubarray2(self, nums: List[int], limit: int) -> int:
        n = len(nums)
        min_dp = [[0 for _ in range(n)] for _ in range(n)]
        max_dp = [[0 for _ in range(n)] for _ in range(n)]
        ans = 1 if 0 <= limit else 0
        for i in range(n):
            min_dp[i][i] = nums[i]
            max_dp[i][i] = nums[i]
        for k in range(2, n+1):
            for i in range(n-k+1):
                j = i + k - 1
                min_dp[i][j] = min(min_dp[i][j-1], nums[j])
                max_dp[i][j] = max(max_dp[i][j-1], nums[j])
                if max_dp[i][j] - min_dp[i][j] <= limit:
                    ans = k
        return ans

