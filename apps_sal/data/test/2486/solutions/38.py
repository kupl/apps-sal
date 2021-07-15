import sys

sys.setrecursionlimit(10 ** 6)
int1 = lambda x: int(x) - 1
p2D = lambda x: print(*x, sep="\n")
def II(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def LI(): return list(map(int, sys.stdin.readline().split()))
def LLI(rows_number): return [LI() for _ in range(rows_number)]
def SI(): return sys.stdin.readline()[:-1]

def main():
    def need(m):
        s=1
        for i in range(n):
            if i==m:continue
            s|=s<<aa[i]
            s&=mask
        #print(m,bin(s),bin(s>>k-aa[m]))
        if s>>k-aa[m]:return True
        return False

    n,k=MI()
    mask=(1<<k)-1
    #print(bin(mask))
    aa=LI()
    aa.sort()
    for i in range(n):
        if aa[i]>k:
            aa=aa[:i]
            break
    n=len(aa)
    #print(aa)
    l=-1
    r=n
    while l+1<r:
        m=(l+r)//2
        #while aa[m-1]==aa[m]:m-=1
        #print(m,aa[m],need(m))
        if need(m):r=m
        else:l=m
    print(l+1)

main()
