class Solution:
    def findslavedays(self,hours):
        a=0
        b=0
        slave=0
        nonslave=0
        slavedays=0
        while b<len(hours):
          #  print(a,b,slave,nonslave,slavedays)
            if slave>nonslave:
                slavedays=max(slavedays,b-a+slave-nonslave-1)
            if a==b:
                if hours[a]<=8:
                    nonslave+=1
                else:
                    slave+=1
                b+=1
                continue
            if slave<nonslave:
                if hours[a]<=8:
                    nonslave-=1
                else:
                    slave-=1
                a+=1
            elif slave>=nonslave:
                if hours[b]<=8:
                    nonslave+=1
                else:
                    slave+=1
                b+=1
            
            if slave>nonslave:
                slavedays=max(slavedays,b-a+slave-nonslave-1)
        print(a,b)
        while a>0:
            a-=1
            if hours[a]<=8:
                nonslave+=1
            else:
                slave+=1
            if slave>nonslave:
                slavedays=max(slavedays,b-a+slave-nonslave-1)
        if slave>nonslave:
                slavedays=max(slavedays,b-a+slave-nonslave-1)        
        return slavedays
    def longestWPI(self, hours: List[int]) -> int:
        isslave=[-1]*len(hours)
        sumslave=0
        for i in range(len(isslave)):
            if hours[i]>8:
                isslave[i]=1
        dic={}
        maxslavedays=0
        print(isslave)
        for i in range(len(isslave)):
            
            sumslave=isslave[i]+sumslave
          #  print(sumslave)
            if sumslave>0:
                maxslavedays=max(maxslavedays,i+1)

            if sumslave not in dic:
                dic[sumslave]=i
            if sumslave-1 in dic:
                
                maxslavedays=max(maxslavedays,i-dic[sumslave-1])
        print(dic)
        return maxslavedays
    
        print(isslave,sumslave)
        a=-1
        b=0
        dic={}
        dic[0]=-1
        for i in range(len(isslave)):
            
            if sumslave[i]>0:
                b=i
                maxslavedays=max(maxslavedays,b-a)
            if sumslave[i]<=0:
                a=i
        return maxslavedays
            
        #for i in range(1,len(isslave)):
            
        return 0
        slavelength1=self.findslavedays(hours)
        slavelength2=self.findslavedays(hours[::-1])
        return max(slavelength1,slavelength2)
