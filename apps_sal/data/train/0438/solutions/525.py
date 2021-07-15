class BinaryIndexedTree:
    ''' index from 1'''
    def __init__(self, n):
        self.n = n
        self.data = [0]*(n+1)
        #todo: init all 1
        for i in range(1, n+1):
            self.data[i]+=1
            tmp = i + (i&-i)
            if tmp <= n:
                self.data[i+(i&-i)] += self.data[i]
    def add(self, index, value):
        while(index<=self.n):
            self.data[index]+=value
            index += index & -index
    def prefix(self, index):
        res = 0
        while(index):
            res += self.data[index]
            index -= index & -index
        return res
    

class Solution:
    def findLatestStep(self, arr: List[int], k: int) -> int:
        n = len(arr)
        if k == n:
            return n
        bit = BinaryIndexedTree(n)
        for no, p in enumerate(arr[::-1]):
            bit.add(p, -1)
            if p-k >= 1:
                s1 = bit.prefix(p-1)
                s2 = bit.prefix(p-k-1)
                if s1 - s2 == k and (p-k-1==0 or bit.prefix(p-k-2)==s2):                    
                    return n-no-1
            if p+k <= n:
                s1 = bit.prefix(p)
                s2 = bit.prefix(p+k)
                if s2 - s1 == k and (p+k==n or bit.prefix(p+k+1)==s2):
                    print('b',p,s1,s2)
                    return n-no-1
        return -1
