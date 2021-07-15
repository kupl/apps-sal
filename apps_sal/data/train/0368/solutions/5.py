class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction.sort()
        
        if satisfaction[0] >= 0:
            return calc_satisfaction(satisfaction)
        
        min_val = -sys.maxsize
        min_index = None
        for i,v in enumerate(satisfaction):
            if 0 > v > min_val:
                min_index = i
                min_val = v
        #curr_satisfaction = calc_satisfaction(satisfaction[min_index+1:])
        curr_sum = sum(satisfaction[min_index+1:])
        while min_index >= 0:
            print((min_index, satisfaction))
            print((satisfaction[min_index], curr_sum))
            if abs(satisfaction[min_index]) < curr_sum:
                curr_sum = curr_sum + satisfaction[min_index]
            else:
                break
            min_index -= 1
        
        print((min_index, satisfaction))
        return calc_satisfaction(satisfaction[min_index+1:])

    
def calc_satisfaction(dishes):
    total = 0
    for i,s in enumerate(dishes):
        total += (i+1) * s
    return total

