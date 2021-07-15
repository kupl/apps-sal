class Solution:
    def numSplits(self, s: str) -> int:
        # set up splitting at idx 1
        p_dict = {s[0]: 1}
        q_dict = {}
        
        for char in s[1:]:
            self.addToDict( q_dict, char )
                
        if ( len(p_dict.keys()) ==  len(q_dict.keys()) ) :
            count = 1
        else:
            count = 0
        
        for i in range(1, len(s) - 1):
            # find the char here
            char = s[i]
            # remove from q, add to p
            self.removeFromDict( q_dict, char)
            self.addToDict( p_dict, char )

            if ( len(p_dict.keys()) ==  len(q_dict.keys()) ):
                count += 1
        
        return count
    
    def addToDict( self, my_dict, value ):
        if (my_dict.get(value) is None):
            my_dict[value] = 1
        else:
            my_dict[value] += 1
    
    def removeFromDict( self, my_dict, value ):
        if (my_dict.get(value) == 1):
            my_dict.pop(value)
        elif (my_dict.get(value) > 1):
            my_dict[value] -= 1
