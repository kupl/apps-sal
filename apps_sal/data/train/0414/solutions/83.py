class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        if(k>len(arr)):
            return max(arr)
        prev = arr[0]
        a = 0
        while(a!=k):
            if(arr[0]>arr[1]):
                if(arr[0]==prev):
                    a+=1
                else:
                    a=1
                    prev = arr[0]
                num = arr.pop(1)
                arr.append(num)
                    
            else:
                if(arr[1]==prev):
                    a+=1
                else:
                    a=1
                    prev = arr[1]
                num = arr.pop(0)
                arr.append(num)
                
        return prev

