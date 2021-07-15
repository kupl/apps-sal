class Solution:
    def numTeams(self, rating: List[int]) -> int:
        sayac = 0
        for i in range(len(rating)):
            temp1 = rating[i]
            for j in range(int(i+1),len(rating)):
                temp2 = rating[j]
                for k in range(int(j+1),len(rating)):
                    temp3 = rating[k]

                    if temp1 > temp2 and temp2 > temp3:
                        sayac+=1
                    if temp3 > temp2 and temp2 > temp1:
                        sayac+=1    
        return sayac

