class Solution:
    def mountain_search(self,start,A):
        valid_mountain = True
        i = start
        while (i < len(A)-1 and A[i] < A[i+1]):
            i+=1
        if (i < len(A)-1 and A[i] != A[i+1]):
            while (i < len(A)-1 and A[i] > A[i+1]):
                i+=1
        else:
            valid_mountain = False
            
        return valid_mountain, i
    
    def longestMountain(self, A: List[int]) -> int:
        # Idea: go through every element in array and try to build largest mountain
        max_mountain = 0
        i = 0
        if not A: return 0
        A.append(A[-1]+1)
        
        while i < len(A)-3:
            if A[i] < A[i+1]:
                valid, new_i = self.mountain_search(i, A)
                if valid:
                    max_mountain = max(max_mountain, new_i-i+1)
                i = new_i
            else:
                i+=1
        return max_mountain
            

