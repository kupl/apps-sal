class Solution:
    def numTeams(self, rating: List[int]) -> int:
        counter = 0
        for i in range(len(rating)):
            for j in range(len(rating)):
                for k in range(len(rating)):
                    # print(f\"Testing: {rating[i]} {rating[j]} {rating[k]}\")
                    if(i < j and j < k):
                        if(rating[i] < rating[j] and rating[j] < rating[k]):
                            # print(f\"Counting up1 {counter}\")
                            counter += 1
                        elif(rating[i] > rating[j] and rating[j] > rating[k]):
                            # print(f\"Counting up2 {counter}\")
                            counter += 1

        return counter
