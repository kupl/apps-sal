class Solution:
    
    def is_unique(self,word):
        count = dict()
        
        for char in ''.join(word):
            if char in count:
                return False
            else:
                count[char] = 1
        
        
        return True
    
    def find_max(self,arr,output,current,start_index):
        if self.is_unique(current):
            output.append(len(''.join(current)))
        
        for i in range(start_index,len(arr)):
            self.find_max(arr,output,current + [arr[i]],i + 1)
        
    
    def maxLength(self, arr: List[str]) -> int:
        
        
        output = []
        
        self.find_max(arr,output,[],0)
        
        return max(output)
