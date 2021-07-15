class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        score = 0
        
        satisfaction.sort()
        print (satisfaction)
        if satisfaction[0] >= 0:
            for i in range(len(satisfaction)):
                score += (i+1) * satisfaction[i]
            return score
        elif satisfaction[len(satisfaction)-1] <= 0:
            return score
        else:
            for i in range(len(satisfaction)):
                score += (i+1) * satisfaction[i]
            
            badDishes = []
            for sat in satisfaction:
                if sat < 0:
                    badDishes.append(sat)
            #print(badDishes)
            for bad in badDishes:
                satisfaction.remove(bad)
                print(satisfaction)
                temp_best = 0
                for i in range(len(satisfaction)):
                    temp_best += (i+1) * satisfaction[i]
                print(temp_best)
                if temp_best > score:
                    score = temp_best
            return score
