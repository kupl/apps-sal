class Solution:
    def knightDialer(self, n: int) -> int:
        self.mod_Val = 10**9 + 7
        self.map = {
            1 : [6,8],
            2 : [7,9],
            3 : [4,8],
            4 : [3,9,0],
            5 : [],
            6 : [1,7,0],
            7 : [2,6],
            8 : [1,3],
            9 : [2,4],
            0 : [4,6],
        }
        self.ans = 0
        self.mem = collections.defaultdict(int)
        for i in range(10):
            self.ans+=self.recursion(n-1, i)
            
        return self.ans%self.mod_Val
        
    def recursion(self, hops, s):
        if not hops:
            return 1
        count = 0
        if (hops, s) not in self.mem:
            for n in self.map[s]:
                count += self.recursion(hops-1, n)
            self.mem[(hops,s)] = count
        
        return self.mem[(hops,s)]
