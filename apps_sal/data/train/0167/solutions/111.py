class Solution:
    def superEggDrop(self, K: int, N: int) -> int:
        cachedSolutions = [[-1 for i in range(N+1)] for j in range(K+1)]
        return self.getMinDrops(K, N, cachedSolutions)

    def getMinDrops(self, eggs, floors, cachedSolutions):
        if cachedSolutions[eggs][floors] > 0:
            return cachedSolutions[eggs][floors]
        elif eggs == 0:
            cachedSolutions[eggs][floors] = 0
            return 0
        elif eggs == 1 or floors <= 2:
            cachedSolutions[eggs][floors] = floors
            return floors
        else:
            ## Arbitrarily large number to initialize the minimum number of drops.
            smallestIndex = 1
            largestIndex = floors
            minDrops = 100000000
            while(smallestIndex<=largestIndex):
                ## We want to find the minimum of the maximums of all possible subproblems and do it through binary search.
                middleIndex = round(smallestIndex+(largestIndex-smallestIndex)/2)
                ## Solve the subproblems.
                minDropsA = self.getMinDrops(eggs-1, middleIndex-1, cachedSolutions)
                minDropsB = self.getMinDrops(eggs, floors-middleIndex, cachedSolutions)
                ## Find a new minimum number of drops for validating that all floors are a solution or not.
                tempMinDrops = max(minDropsA, minDropsB) + 1
                minDrops = min(minDrops, tempMinDrops)
                ## Check which half will contain the valid solution.
                if (minDropsA > minDropsB):
                    largestIndex = middleIndex - 1
                else:
                    smallestIndex = middleIndex + 1
            cachedSolutions[eggs][floors] = minDrops
        return cachedSolutions[eggs][floors]


