class Solution:
    def dieSimulatorLast(self, n, rollMax, last, count):
        # n: number of rolls
        # rollMax: 
        # last: the last number in the sequence
        # count: how many times `last` occurs consecutively in the sequence
        if count > rollMax[last]:
            return 0
        elif n == 0:
            return 1
        elif self.result[last][count][n] != -1:
            return self.result[last][count][n]
        
        temp = 0
        for i in range(6):
            if i == last:
                temp += self.dieSimulatorLast(n-1,rollMax,i,count+1)
            else:
                temp += self.dieSimulatorLast(n-1,rollMax,i,1)
        self.result[last][count][n] = temp % 1000000007
                
        return temp % 1000000007
        
    def dieSimulator(self, n: int, rollMax: List[int]) -> int:
        self.result = [[[-1 for i in range(n+1)] for j in range(17)] for k in range(6)]
        return self.dieSimulatorLast(n, rollMax, 0, 0)

