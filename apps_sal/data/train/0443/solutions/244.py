class Solution:
    
    def checkList(self, head: List[List[int]], tail: List[int], init: int) -> int:
        result = init
        head_copy = head.copy()
        for i in head_copy:
            num = tail[0]
            ilen = len(i)
            if ilen == 2:
                if (i[0] < i[1] and i[1] < num) or (i[0] > i[1] and i[1] > num):
                    result+=1   
            elif ilen < 2:
                head.append(i + [num])    

        if len(tail) == 1: 
            return result
        else:
            return self.checkList(head, tail[1:], result)
        
    def numTeams(self, rating: List[int]) -> int:
        if len(rating) < 3: 
           return 0 
        return self.checkList([[]], rating, 0)    
