import sys

def main():
    t = sys.stdin.readline().split()
    n = int(t[0])
    h = int(t[1])
    k = int(t[2])
    line = sys.stdin.readline()
    x = list(map(int,line.split()))
    
    res = 0
    cur = 0
    for i in range(n):
        cur += x[i]
        if i!=n-1:
            if x[i+1]+cur <= h:
                continue        
        v = int(cur/k)
        if v*k != cur :
            cur = cur - v*k
            res+= v
            if i!=n-1:
                if x[i+1]+cur > h:
                    res+=1
                    cur=0
            else:
                res+=1
        else :
            cur =0
            res +=v
        
    print(res)

main()
