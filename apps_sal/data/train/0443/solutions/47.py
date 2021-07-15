class Solution:
    def numTeams(self, rating: List[int]) -> int:
        temp_list = []
        temp1 = 0
        temp2 = 0
        for i in range(0,len(rating)):
            temp1 = rating[i]
            for j in range(i+1,len(rating)):
                if rating[j]>temp1:
                    temp2 = rating[j]
                    for k in range(j+1,len(rating)):
                        if rating[k] > temp2:
                            temp_list.append([temp1,temp2,rating[k]])
            for j in range(i+1,len(rating)):
                if rating[j]<temp1:
                    temp2 = rating[j]
                    for k in range(j+1,len(rating)):
                        if rating[k] < temp2:
                            temp_list.append([temp1,temp2,rating[k]])
        return len(temp_list)
