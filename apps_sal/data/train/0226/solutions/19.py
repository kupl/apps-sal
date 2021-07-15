


def getPermutations(array):
    ans = set()
    def helper(arr,i,ans):
        if i==len(arr)-1:

            ans.add(tuple(arr))
            return
        
        for j in range(i,len(arr)):
            if not (arr[i]==arr[j] and i!=j):
                test = (i<=1) or (((arr[i-1]+arr[i-2])**0.5)==int((arr[i-1]+arr[i-2])**0.5))
                swap(arr,i,j)
                if (test):
                    helper(arr,i+1,ans)
            
                swap(arr,i,j)
            
    def swap(arr,i,j):
        arr[i],arr[j]=arr[j],arr[i]
        
    helper(array,0,ans)
    return ans

class Solution:
    
    
    
    def numSquarefulPerms(self, A: List[int]) -> int:
        va = getPermutations(A)
        
        valid = 0
        # print(va)
        for a in va:
            isValid = True
            # print(a)
            for idx in range(1,len(a)):
                
                if ((a[idx]+a[idx-1])**0.5)!=int((a[idx]+a[idx-1])**0.5):
                    # print(a,idx)
                    isValid = False
                    break
                    
            if isValid:
                # print(a)
                valid+=1
                
        # print(valid)
        return valid
        

