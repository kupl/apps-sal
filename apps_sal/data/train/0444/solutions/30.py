class Solution:
    def nthPersonGetsNthSeat(self, n: int) -> float:
        if n == 1:
            return 1
        
        # Create a list of probablity of n-th person get his own seat under the situation 1-st person pick k-th seat
        pick = [1] + [0]*(n - 2) + [1]
        
        prob = 0
        for i in range(n-2, 0, -1):
            left = n - i
            pick[i] = 1/left + ((left-2)/left)*pick[i+1]
            prob += pick[i]
        
        return (prob+1)/n
