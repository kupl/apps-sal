class Solution:

    def numTimesAllBlue(self, light: List[int]) -> int:
        """arr=[0]*(len(light)+1)
        cnt=0
        max_1=light[0]
        i=0
        while i<len(light):
            arr[light[i]]=1           
            if max_1<light[i]:
                max_1=light[i] 
            if sum(arr)==max_1:
                cnt+=1
            i+=1
        return(cnt)"""
        cnt = 0
        max_1 = light[0]
        for i in range(0, len(light)):
            max_1 = max(max_1, light[i])
            if max_1 == i + 1:
                cnt += 1
        return cnt
