import sys
import numpy as np
def input(): return sys.stdin.readline().rstrip()

def kosuu(x):
    re = [0,0]
    while x % 2 == 0:
        x = x//2
        re[1]+=1
    re[0]=x
    return re

        
 
def main():
    n,m=map(int, input().split())
    a=list(map(int, input().split()))
    li = [kosuu(a[0])[0]]
    hantei = kosuu(a[0])[1]
    for i in a[1:]:
        hantei2 = kosuu(i)
        if hantei2[1] != hantei:
            print(0)
            break
        else:
            li.append(hantei2[0])
    else:
        lc = np.lcm.reduce(li)
        print(((m//(lc*2**(hantei-1)))+1)//2)
            


def __starting_point():
    main()
__starting_point()
