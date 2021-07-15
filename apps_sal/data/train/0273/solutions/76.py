class Solution:
    def racecar(self, target: int) -> int:
        a,d,m,s=[(0,1)],set([(0,1)]),2*target,0
        while 1:
            b,s=[],s+1
            for i,j in a:
                ii,jj,k=i+j,2*j,-1 if j>0 else 1
                if ii==target: return s
                if (ii,jj) not in d and 0<ii<m:
                    b.append((ii,jj))
                    d.add((ii,jj))
                if (i,k) not in d:
                    b.append((i,k))
                    d.add((i,k))
            a=b
