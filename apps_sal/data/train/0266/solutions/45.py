from collections import Counter

class Solution:
    def numSplits(self, s: str) -> int:
        #pseudo:
        #start left window at 0
        #have right window open for all letters in s
        #keep count for left and right
        #keep overall count
        #left woud start with first letter, right would be rest of letters
        #loop through each letter
        #left window should increase by one [i+1]
        #right window should decrease by 1
        #if the letter in the right dictionary already exists, then remove and decrease the right count             by 1
        #if current letter not in the left dictionary then +1 to left count and add to dictionary 
        #if left count and right counter are both equal to each other then add 1 to count 
        
        l_dict = Counter()
        r_dict = Counter(s)
        counter = 0
        
        print(r_dict)
        for i in s:
            r_dict[i] -= 1
            l_dict[i] = l_dict.get(i, 0) + 1
            
            if r_dict[i] == 0:
                del r_dict[i]
                
            if len(l_dict) == len(r_dict):
                counter += 1
                
        return counter
        

