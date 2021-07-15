class Solution:
    def mergeSort(self, lst: List[int]) -> int:
        n = len(lst)
        
        # base case
        if n <= 1:
            return lst
        
        mid = n // 2
        L   = lst[:mid]
        R   = lst[mid:]
        
        self.mergeSort(L)
        self.mergeSort(R)
        
        i, j, k = 0, 0, 0
        while (i < len(L)) and (j < len(R)):
            if (L[i] < R[j]):
                lst[k] = L[i]
                i += 1
                
            else:
                lst[k] = R[j]
                j += 1
                
            k += 1
        
        # fill remaining
        while (i < len(L)):
            lst[k] = L[i]
            i += 1
            k += 1
            
        while (j < len(R)):
            lst[k] = R[j]
            j += 1
            k += 1 
        
        return lst
    
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        n = len(satisfaction)
        possible_sums = [None for i in range(n)]
        print('.......')
        self.mergeSort(satisfaction)
        print(satisfaction)
        
        for i in range(n):
            arr = satisfaction[i:]
            like_times = [((j+1) * arr[j]) for j in range(len(arr))]
            possible_sums[i] = sum(like_times)
        
        return max(max(possible_sums), 0)
        
        

