def increasecheck(List,second_index):
    count=0
    for i in List[second_index+1:]:
        if i>List[second_index]:
            
            count+=1
    return count
def decreasecheck(List,second_index):
    count=0
    for i in List[second_index+1:]:
        if i<List[second_index]:
            
            count+=1
    return count
class Solution:
    
    def numTeams(self, rating: List[int]) -> int:
        n=len(rating)
        output=0
        for i in range(n):
            for j in range(n-1):
                if i>j:
                    continue
                if rating[i]>rating[j]:
                    
                    output+=decreasecheck(rating,j)
                    
                if rating[i]<rating[j]:
                    output+=increasecheck(rating,j)
        return output

