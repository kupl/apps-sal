class Solution:
    def minNumberOfFrogs(self, croakOfFrogs: str) -> int:
        frog_counter = 0  # To count the minimum no. of frogs croaking
        crk_dict = {'c':0,'r':0,'o':0,'a':0,'k':0} # create dictionary initializing the values to 0
        
        # The string must always start with 'c'
        if croakOfFrogs[0] != 'c':
            return (-1)
        
        # The string must always end with 'k'
        elif croakOfFrogs[-1] != 'k':
            return (-1)
        
        else:
            for i in range(len(croakOfFrogs)):
                # As the craok always start with c and the characters are sequential always the count of each of the char should greater than or equal to the next char of string 'craok'
                if crk_dict['c'] >= crk_dict['r'] >= crk_dict['o'] >= crk_dict['a'] >= crk_dict['k']:
                    
                    crk_dict[croakOfFrogs[i]] += 1
                    
                    # if 'c' is encountered in string before the completion of croak, that mean it is the other frog, hence add 1 to the frog counter
                    if frog_counter < crk_dict['c']:
                        frog_counter += 1
                        
                    # if the iterable gets 'k' that means the frog is free to croak again
                    if croakOfFrogs[i] == 'k':
                        for m in crk_dict:
                            crk_dict[m] -= 1
                else:
                    return (-1)
            return frog_counter
