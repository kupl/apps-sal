class Solution:
    def maxLength(self, arr: List[str]) -> int:
        def isUnique(concatString):
            concatSet = set()
            for char in concatString:
                if char in concatSet:
                    return False
                concatSet.add(char)
            return True
        
        length = len(arr)
        self.result = 0
        def dfs(index, curr):
            if isUnique(curr):
                self.result = max(self.result, len(curr))
            if index == length - 1:
                return
            for i in range(index + 1, length):
                dfs(i, curr + arr[i])
        
        for i in range(length):
            dfs(i, arr[i])
            
        return self.result
        
        

