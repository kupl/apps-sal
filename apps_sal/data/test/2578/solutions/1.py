import sys
input = iter(sys.stdin.read().splitlines()).__next__

class mergefind:
    def __init__(self,n):
        self.parent = list(range(n))
        self.size = [1]*n
        self.num_sets = n

    def find(self,a):
        to_update = []
       
        while a != self.parent[a]:
            to_update.append(a)
            a = self.parent[a]
       
        for b in to_update:
            self.parent[b] = a

        return self.parent[a]

    def merge(self,a,b):
        a = self.find(a)
        b = self.find(b)

        if a==b:
            return

        if self.size[a]<self.size[b]:
            a,b = b,a

        self.num_sets -= 1
        self.parent[b] = a
        self.size[a] += self.size[b]

    def set_size(self, a):
        return self.size[self.find(a)]

    def __len__(self):
        return self.num_sets

n,m = list(map(int,input().split()))
mf = mergefind(n)

for _ in range(m):
    sz,*A = [int(x)-1 for x in input().split()]
    sz += 1

    for i in range(1,sz):
        prev,cur = A[i-1],A[i]
        mf.merge(prev,cur)

print(*[mf.set_size(i) for i in range(n)])

