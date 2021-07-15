class Solution:
    def canReorderDoubled(self, A: List[int]) -> bool:
        
        A.sort() 
        map = {}
        
        for item in A:
            if item in map : map[item] +=1
            else : map[item] =1
        
        for item in A:
            if map[item]==0 : continue
            if item <0 :
                if item/2 in map : 
                    if map[item/2]==0 : return False
                    map[item] -=1
                    map[item/2] -=1
                else : return False
            else :
                if item *2 in map:
                    if map[2*item]==0: return False
                    map[item] -=1
                    map[item*2] -=1
                else : return False
        
        return True
