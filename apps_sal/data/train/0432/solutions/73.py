class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        freq = {}
        nums.sort()
        for n in nums:
            if n in freq:   
                freq[n]+=1
            else:
                freq[n]=1
        for num in freq:
            if freq[num]!=0:
                temp = freq[num]
                for i in range(num,num+k):
                    if i not in freq or freq[i]<temp:
                        return False
                    else:
                        freq[i]-=temp
        return True

