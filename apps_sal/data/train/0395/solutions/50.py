class Solution:
    def oddEvenJumps(self, A: List[int]) -> int:
        nums_in = sorted((num, index) for index, num in enumerate(A))
        print(nums_in)
        index_in = self.helper(nums_in)
        
        nums_de = sorted((-num, index) for index, num in enumerate(A))
        index_de = self.helper(nums_de)
        
        greater = [False] * len(A)
        smaller = [False] * len(A)
        
        greater[-1] = True
        smaller[-1] = True
        
        for i in range(len(A) - 2, -1, -1):
            greater[i] = smaller[index_in[i]]
            smaller[i] = greater[index_de[i]]
        
        return sum(greater)
        
    
    def helper(self, nums):
        result = [0] * len(nums)
        queue = list()
        
        for (_, index) in nums:
            while queue and index > queue[-1]:
                result[queue.pop()] = index
            queue.append(index)
        
        return result
    
    

