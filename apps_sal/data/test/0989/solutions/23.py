'''
Fuad Ashraful Mehmet
Bsc in CSE
University of Asia Pacific
Dhaka,Bangladesh

problem:from code forces


'''
# install xampp https://vitux.com/how-to-install-xampp-on-your-ubuntu-18-04-lts-system/




class Solve():
    
    def __init__(self):
        self.n,self.k=map(int,input().split())
        self.fuad=list(map(int,input().split()))
        self.fuad.sort()
    def FuckCase(self):
        
        for i in range(int(self.n/2)):
            
            s=(self.fuad[i+1]-self.fuad[i])*(i+1)+(self.fuad[self.n-i-1]-self.fuad[self.n-i-2])*(i+1)

            # print("i {} j {} s {} k {}".format(i,self.n-i-1,s,self.k))
            if s<=self.k:
                self.k-=s
            else:
                print(self.fuad[self.n-i-1]-self.fuad[i]-int((self.k/(i+1))))
                return


        print("0")



obj =Solve()

obj.FuckCase()
