class Solution:
    def numTeams(self, r: List[int]) -> int:
        c=0
        for i in range(len(r)-2):
            for j in range(i+1,len(r)-1):
                for k in range(j+1,len(r)):
                    if(r[i]>r[j]>r[k]) or (r[i]<r[j]<r[k]):
                        c+=1
        return c
                        

