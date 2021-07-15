#SELF TRY 9/20/2020
class Solution:
    def longestArithSeqLength(self, A: List[int]) -> int:
        #Problem asks -> array A 
        #Want -> return the length of longest arithmetic subseq in A 
        
        #Two cases basically.
        #When building up to to your table 
        #When looking at previous values i.e from (col, change) we see that there is a PREVIOUS value already there. (With the same change) so you know you can extend that length by 1
        #This \"1\" indicates the CUR number is being added because it's change is the same. 
        #If it's never been seen that the base case is at most length 2 
        #i.e some \"subseq\" whatever it is with 2 elements would always be \"valid\" and so would be length 2 
        table = dict()
        longest_subseq = float('-inf')
        
        for row in range(len(A)): 
            for col in range(0, row): 
                change = A[row] - A[col]
                if (col, change) in table: 
                    table[(row, change)] = 1 + table[(col, change)]
                    
                
                
                else: 
                    table[(row, change)] = 2 
                longest_subseq = max(longest_subseq, table[(row, change)])
        return longest_subseq

