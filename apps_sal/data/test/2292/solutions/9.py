from collections import defaultdict
import sys

int1 = lambda x: int(x) - 1
p2D = lambda x: print(*x, sep="\n")
def II(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def LI(): return list(map(int, sys.stdin.readline().split()))
def LLI(rows_number): return [LI() for _ in range(rows_number)]
def SI(): return sys.stdin.readline()[:-1]

def main():
    for _ in range(II()):
        n = II()
        aa = LI()
        bb = LI()

        if n%2:
            if aa[n//2]!=bb[n//2]:
                print("No")
                continue

        cnt=defaultdict(int)
        for i in range(n//2):
            l=aa[i]
            r=aa[n-1-i]
            if l>r:l,r=r,l
            cnt[l,r]+=1

        ng=False
        for i in range(n//2):
            l=bb[i]
            r=bb[n-1-i]
            if l>r:l,r=r,l
            if cnt[l,r]==0:ng=True
            cnt[l,r]-=1

        if ng:print("No")
        else:print("Yes")

main()

