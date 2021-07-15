class Solution:
    
    def checkList(self, head: List[List[int]], tail: List[int], init: int) -> int:
        result = init
        head_copy = list(head)
        num = tail[0]
        
        for i in head_copy:
            if len(i) == 2:
                if (i[0] < i[1] and i[1] < num) or (i[0] > i[1] and i[1] > num):
                    result+=1   
            else:
                head.append(i + [num])    

        if len(tail) == 1: 
            return result
        else:
            return self.checkList(head, tail[1:], result)
        
    def numTeams(self, rating: List[int]) -> int:
        if len(rating) < 3: 
           return 0 
        return self.checkList([[],[rating[0]]], rating[1:], 0)   
