class Solution:
    def minSteps(self, s: str, t: str) -> int:
        steps = 0
        myDict = {}
        
        # create a dictionary with keys from s and how many times they occur
        for c in s:
            if c in myDict:
                myDict[c] += 1
            else:
                myDict[c] = 1
                
        
        for c in t:
            # if the key exists we decrement the value that the key holds
            if c in myDict:
                myDict[c] -= 1
                if myDict[c] == 0:
                    del myDict[c]
            # if the key does not exist then we increment steps by 1
            else:
                steps += 1
                
        return steps

