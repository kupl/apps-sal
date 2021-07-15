class Solution:
    def maxLength(self, arr: List[str]) -> int:
            
        # backtracking function
        
        def helper(arr, substring, i):
            
            # get the length of the substring without char duplication 
            unique_length = len(set(substring))
            
            # if there is no duplicate chars
            if len(substring) == unique_length:
                self.max_len = max(self.max_len, unique_length)
            
            # check if we reached the last substring in arr
            if i == len(arr) - 1:
                return

            for j in range(i+1, len(arr)):
                helper(arr, substring + arr[j], j)

            return
        
        
        self.max_len = 0
        
        helper(arr, '', -1)
        
        return self.max_len
