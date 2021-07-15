import math
class Solution:
    squares=[]
    dp={}
    def util(self,n):
        if n==0:
            return False
        if n in self.dp:
            return self.dp[n]
        
        for i in range(1,int(math.sqrt(n))+1):
          #  print(\"square we subtract is\",self.squares[i],\"in util of\",n,\"and checking if util of\",n-self.squares[i],\"is true or false\")
            if not self.util(n-self.squares[i]):
        #        print(\"util of\",n-self.squares[i],\"turned out to be false,so util of\",n,\"is a win!\")
                self.dp[n]=True
                return True
       # print(\"all paths from util of\",n,\"led to failure, and we lost GG\")
        self.dp[n]=False
        return False
                
    def winnerSquareGame(self, n: int) -> bool:
        self.squares=[]
        for i in range(int(math.sqrt(n))+1):
            self.squares.append(i*i)
        return self.util(n)
