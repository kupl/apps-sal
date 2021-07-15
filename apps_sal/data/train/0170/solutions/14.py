from bisect import bisect_left as bl ,bisect_right as br,bisect as bis,insort_left as il,insort_right as ir ,insort as isrt
class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        
        maxarr=[1]
        n=len(arr)
        flag=0
        
        for i in range(1,n):
            if (arr[i]>=arr[i-1]):
                maxarr.append(maxarr[-1]+1)
            else:
                flag=1
                maxarr.append(1)
        if flag ==0:
            return 0
        arr1=[arr[0]]
        arr2=[arr[-1]]
        
        i=1
        while i<len(arr) and maxarr[i]>maxarr[i-1]:
            arr1.append(arr[i])
            i+=1
        
        i=len(arr)-2
        while i >=0 and maxarr[i]<maxarr[i+1]:
            arr2.append(arr[i])
            i-=1
        
        
        print((arr1, arr2[::-1]))
        arr2= arr2[::-1]
        size = len(arr2)
        maxm = len(arr1)
        for i in arr2:
            index = br(arr1 , i)
            maxm = max(index +size ,maxm)
            size-=1
     
            
            
                    
        
        
        return len(arr)-maxm
            
      
        
            
                
        

