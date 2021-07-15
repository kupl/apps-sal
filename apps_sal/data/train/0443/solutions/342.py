class Solution:
    def numTeams(self, rating: List[int]) -> int:
        if not(rating): return 0
        
        asc, desc = 0, 0
        for index in range(len(rating)):
            lrd, lri, rld, rli = 0, 0, 0, 0
            for num in rating[:index]:
                if num<rating[index]:
                    lri += 1
                elif num>rating[index]:
                    lrd += 1
            
            for num in rating[index:]:
                if num>rating[index]:
                    rli += 1
                elif num<rating[index]:
                    rld += 1            
            
            asc += lri * rli
            desc += lrd * rld
        
        return asc+desc

