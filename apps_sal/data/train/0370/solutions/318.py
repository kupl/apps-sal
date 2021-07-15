import math
import collections
class Solution:
    def largestComponentSize(self, A) -> int:
        self.pre = {}
        for i in A:
            for d in range(2,int(math.sqrt(i)+1))[::-1]:
                if i%d == 0:
                    self.union(self.find(i),self.find(d))
                    self.union(self.find(i),self.find(i//d))
        count = collections.defaultdict(int)
        for i in A:
            count[self.find(i)] += 1
        return max(count.values())   
    def find(self,x):
        if x not in self.pre:
            self.pre[x] = x
        while self.pre[x] != x:
            self.pre[x] = self.pre[self.pre[x]]
            x = self.pre[x]
        return x
        
    def union(self,x,y):
        if self.pre[x] == self.pre[y] :return
        fx = self.find(x)
        fy = self.find(y)
        self.pre[fy] = fx
