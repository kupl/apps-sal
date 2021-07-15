class Solution:
    def maxLength(self, arr: List[str]) -> int:
        if len(arr)==1:
            if len(set(arr[0]))==len(arr[0]):
                return len(arr[0])
            else:
                return 0
        
        new_arr = []
        for s in arr:
            if len(s) == len(set(s)):
                new_arr.append((set(s), len(s)))
                
        if not new_arr:
            return 0
        # print(new_arr)
        ans = 0
        
        def backtrack(ind, temp, temp_sum):
            nonlocal ans
            if temp_sum > ans:
                ans = temp_sum
                
            for i in range(ind, len(new_arr)):
                if not (new_arr[i][0] & temp):
                    backtrack(i+1, temp | new_arr[i][0], temp_sum+new_arr[i][1])
                else:
                    backtrack(i+1, temp, temp_sum)
                    
        backtrack(0, set(), 0)
        return ans
