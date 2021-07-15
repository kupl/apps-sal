class Node:
    def __init__(self,data):
        self.data=data
        self.p=None
    
class Solution:
    def find(self,node):
        if(node.p==node):
            return node
        node.p=self.find(node.p)
        return node.p
    
    def prime(self,val,d):
        for i in range(2,int((val)**(0.5))+1):
            if(val%i==0):
                if(i not in d):
                    node=Node(i)
                    node.p=node
                    d[i]=node
                    
                if(self.find(d[val].p)==d[val]):
                    d[val].p=d[i]
                else:
                    self.find(d[i]).p=self.find(d[val])
                v=val//i
                if(v!=i):
                    if(v not in d):
                        node=Node(v)
                        node.p=node
                        d[v]=node
                    self.find(d[v]).p=self.find(d[val])
                    
    def largestComponentSize(self, A: List[int]) -> int:
        d={}
        if(not A):
            return 0
        for i in A:
            if(i not in d):
                node=Node(i)
                node.p=node
                d[i]=node
            self.prime(i,d)
        fr=defaultdict(int)
        
        for i in A:
            fr[self.find(d[i]).data]+=1
        mx=0
        for i in fr.values():
            mx=max(i,mx)
        return mx
