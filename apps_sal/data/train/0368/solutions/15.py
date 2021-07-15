class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction.sort()
        total = 0
        beneficial = deque()
        negative = []
        def calc_satisfaction(dishes):
            total = 0
            for i,s in enumerate(dishes):
                total += (i+1) * s
            return total
        
        for s in satisfaction:
            if s >= 0:
                beneficial.append(s)
            else:
                negative.append(s)

        curr_satisfaction = calc_satisfaction(beneficial)
        for s in reversed(negative):
            temp_satisfaction = calc_satisfaction(deque([s]) + beneficial)
            if temp_satisfaction > curr_satisfaction:
                curr_satisfaction = temp_satisfaction
                beneficial.appendleft(s)
            else:
                break
                
        return curr_satisfaction

    


