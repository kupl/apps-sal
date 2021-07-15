import sys
from collections import defaultdict
from heapq import heappop,heappush

def main():
    n = int(sys.stdin.readline())
    h = []
    d = sys.stdin.readlines()
    res = []
    for i in range(n):
        x = d[i].split()
        if x[0]=="insert":
            t = int(x[1])
            heappush(h,t)
        elif x[0] == "getMin":
            t = int(x[1])
            while len(h)>0 and h[0]<t:
                res.append("removeMin")
                heappop(h)
                
            if len(h)==0 or h[0]>t:
                res.append("insert "+x[1])
                heappush(h,t)
            
        elif x[0] == "removeMin":
            if len(h)==0:
                res.append("insert 0")  
            else:
                heappop(h)              
                
        res.append(d[i].rstrip())

    print(len(res))
    print("\n".join(res))

main()

