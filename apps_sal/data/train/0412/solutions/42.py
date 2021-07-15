class Solution:
    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        bottomWidth = f + ((d-1)*(f-1))
        currentLayer = [0 for i in range(bottomWidth)] + [1 for i in range(f)] + [0 for i in range(bottomWidth)]
        nextLayer = []
        
        for run in range(d-1): # runs as many times as we traverse down the triangle
            # update each next layer number to be sum of f numbers above it
            for i in range(f, len(currentLayer)-f):
                localSum = 0
                for j in range(i, f+i):
                    localSum += currentLayer[j]
                nextLayer += [localSum]
                
            neededZeros = [0 for i in range((len(currentLayer) - len(nextLayer))//2)]
            currentLayer = neededZeros + nextLayer + neededZeros
            nextLayer = []
            
        # at this point, shave off the zeros
        while 0 in currentLayer:
            currentLayer.remove(0)
            
        # at this point, the answer must be less than or equal to d, and greater than or equal to f*d.
        if target-d >= len(currentLayer): 
            return 0
        else: 
            return currentLayer[target-d] % ((10**9) + 7)
