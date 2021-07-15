class Solution:
    def numTeams(self, rating: List[int]) -> int:
       
        def getTeams(k, l, prev = None, asc=True):
            if (k>len(l)):
                return 0
            if ((prev is None) & (k == 1)):
                return len(l)
            if (k == 1):
                if asc: 
                    teamCount = sum([x>prev for x in l])
                else:
                    teamCount = sum([x<prev for x in l])
            else:
                teamCount = 0
                larger_x = True
                if prev is not None:
                    larger_x = l[0]>prev
                    
                if asc:
                    if (larger_x | (prev is None)):
                    #include this one
                        teamCount +=getTeams(k-1, l[1:], l[0], asc)
                    #exclude this one
                    teamCount +=getTeams(k, l[1:], prev, asc)
                        
                else:
                    if (larger_x == False | (prev is None)):
                        #print(prev, l[0], larger_x)
                    #include this one
                        teamCount +=getTeams(k-1, l[1:], l[0], asc)
                    #exclude this one
                    teamCount +=getTeams(k, l[1:], prev, asc)
            #print('getTeams: ', k, l, prev, asc,'   result: ', teamCount)
            return teamCount
        
        return getTeams(3, rating, None, True) + getTeams(3, rating, None, False)
