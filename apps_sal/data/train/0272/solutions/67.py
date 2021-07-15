class Solution:
    def maxCandies(self, status: List[int], candies: List[int], keys: List[List[int]], containedBoxes: List[List[int]], initialBoxes: List[int]) -> int:
        if len(initialBoxes) == 0:
            return 0
        else:
            boxdict = {}
            candysum = 0
            
            for initialbox in initialBoxes:
                boxdict[initialbox] = [0,0]
            
            p = len(status)**2
            while p > 0:
                for i in range(len(containedBoxes)):
                    if i in boxdict:
                        for containedbox in containedBoxes[i]:
                            boxdict[containedbox] = [0,0]
                        p -= 1
            
            for j in range(len(keys)):
                for boxedkeys in keys[j]:
                    if boxedkeys in boxdict:
                        boxdict[boxedkeys][1] = 1
                        
            for l in range(len(status)):
                if status[l] == 1 and l in boxdict:
                    boxdict[l][0] = 1
            
            for key in boxdict:
                if (boxdict[key][0] == 1 and boxdict[key][1] == 1) or (boxdict[key][0] == 1 or boxdict[key][1] == 1):
                    candysum += candies[key]
            
            return candysum

