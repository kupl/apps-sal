class Solution:
    def numTeams(self, rating: List[int]) -> int:
        count=0
        for i in range(len(rating)):
            for j in range(i+1,len(rating)):
                for k in range(j+1,len(rating)):
                    if self.check(rating[i],rating[j],rating[k]):
                        # print(rating[i],rating[j],rating[k])
                        count+=1
        return count
    
    def check(self,i,j,k):
        if i<j and j<k:
            return True
        elif i>j and j>k:
            return True
        else:
            return False
