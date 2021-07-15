#educational round 29
#two robots play N rounds of game 1 2 3. each choose a number from 1 2 or 3
#game rule 3 win 2, 2 win 1, 1 win against 3
#player choose next number from previous move of both players.
#input format
#line 1:     N a b - N round of games, a b is the number of first round from alice and bob
#line 2 - 4: 3 x 3 grid Aij is next number of Alice if previous A=i, B=j
#line 5 - 7: 3 x 3 grid Bij is next number of Bob if previous A=i, B=j
#output format
#total points of Alice and Bob
class Game123:
    def __init__(self):
        self.alice = [0]*9
        self.bob=[0]*9
        self.moves=[-1]*10
        self.count=0
        self.pointsA=0
        self.pointsB=0

    #convert 3x3 grid into 1D array
    def gameChoice(self, m, r, bBob):
        choice=self.alice
        if bBob:
            choice=self.bob
        for i in range(len(m)):
            choice[3*r+i]=m[i]

    #look if move already exists
    def findMove(self, a, b):
        m=(a-1)*3+b-1
        for i in range(self.count):
            if self.moves[i]==m:
                return i
        #print("a={0} b={1} m={2} count={3}".format(a,b,m, self.count))
        self.moves[self.count]=m
        self.count += 1
        return -1

    def computePoints(self, m):
        #convert m back to a and b, m is  from 0 to 8
        b=m%3+1
        a=m//3+1
        #return positive if alice win
        if a==b:
            return
        if a==3 and b==2 or a==2 and b==1 or a==1 and b==3:
            self.pointsA += 1
        else:
            self.pointsB += 1

    def output(self):
        print("{0} {1}".format(self.pointsA,self.pointsB))    
        
    def startGame(self, a, b, totalmoves):
        #print(self.moves)
        #print(self.alice)
        #print(self.bob)
        found=-1
        while found<0:
            found=self.findMove(a,b)
            m=(a-1)*3+b-1
            a=self.alice[m]  #next move
            b=self.bob[m]
        #print("repeat {0} to {1}".format(found, self.count))
        pointaA=0
        pointsB=0
        # compute moves of no repeats
        if totalmoves <= self.count:
            for i in range(totalmoves):
                self.computePoints(self.moves[i])
        else:
            totalmoves -= found
            repeats = totalmoves//(self.count-found)
            totalmoves %= (self.count-found)
            for i in range(found, self.count): #repeated moves
                self.computePoints(self.moves[i])
            #self.output()
            self.pointsA *= repeats
            self.pointsB *= repeats
            #self.output()
            for i in range(found): #moves before repeat
                self.computePoints(self.moves[i])
            #self.output()
            for i in range(found, totalmoves+found): #odd moves after repeat
                self.computePoints(self.moves[i])
        self.output()

    def test():
        g=Game123()
        g.gameChoice([2,2,1],0,False)
        g.gameChoice([3,3,1],1,False)
        g.gameChoice([3,1,3],2,False)
        g.gameChoice([1,1,1],0,True)
        g.gameChoice([2,1,1],1,True)
        g.gameChoice([1,2,3],2,True)
        g.startGame(1,1,8)

def nia():
    s=input()
    while len(s)==0:
        s=input()
    s=s.split()
    iVal=[];
    for i in range (len(s)):
        iVal.append(int(s[i]))
    return iVal

def solve():
    g=Game123()
    nab=nia()
    for i in range(3):
        g.gameChoice(nia(), i, False)
    for i in range(3):
        g.gameChoice(nia(), i, True)
    g.startGame(nab[1],nab[2],nab[0])
    
solve()  

