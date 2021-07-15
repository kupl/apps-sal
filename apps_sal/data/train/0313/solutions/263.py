class Solution:
    def checkDay(self,day,bloomDay,m,k)->bool:
        y,count=0,0
        for i in range(len(bloomDay)):
            if bloomDay[i] <= day:
                #bloomed.append(1)
                y+=1
            else:
                #bloomed.append(0)
                y=0
            if y==k:
                count+=1
                y=0
            if count==m:
                return True
        return False
    
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        '''
        bloomDay: Flower garden, elements are # of days required for that flower to bloom
        m: # of bouquets needed
        k: # of adjacent flowers needed in each bouquet
        First, check to see if mk>len(bloomDay). If so return -1
        Then, see how many days needed until mk flowers have bloomed
            Check to see if they are adjacent
            if so return days
            else maybe check how many adjacents are needed, or go to the next day
        
        '''
        #bloomDay,m,k = [7,7,7,7,12,7,7],2,3
        
        FN=m*k # (Flowers Needed)
        if FN > len(bloomDay):
            return -1
        
        
        # After x days, is it possible to create m bouquets?
        
        
        bloomed=sorted(bloomDay)
        lastWorking,count,start,stop=-1,0,0,len(bloomed)
        #print(bloomed)
        half=stop//2
        #day=bloomed[half]
        while(start<=half<stop):
            day=bloomed[half]
            #print('Half: ',half,', Day: ',day,' || Bounds: ',start,', ',stop)
            
            # If current day works, check previous day
            if self.checkDay(day,bloomDay,m,k):
                #print('Day:  ',day,' works')
                lastWorking,stop=day,half
            # Otherwise check half of new bounds
            else:
                start=half+1
            half=(start+stop)//2
            
        return lastWorking
