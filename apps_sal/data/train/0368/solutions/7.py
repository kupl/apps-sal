class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction.sort()
        s = 0
        counter = 1
        for i in satisfaction:
            s += i * counter
            counter += 1
        check = s
        longest = s
        while True:
            s = 0
            counter = 1
            for i in satisfaction:
                s += i * counter
                counter += 1
            if s < check:
                return check
            if s > check:
                longest = s
            check = s
            if len(satisfaction) == 0:
                return longest
            satisfaction = satisfaction[1:]
