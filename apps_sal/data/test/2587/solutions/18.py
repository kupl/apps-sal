# -*- coding: utf-8 -*-
"""
@author: Saurav Sihag
"""

rr = lambda: input().strip()
rri = lambda: int(rr())
# rri = lambda: int(stdin.readline())
rrm = lambda: [int(x) for x in rr().split()]
# stdout.write(str()+'\n')

from sys import stdin, stdout, setrecursionlimit

def sol():
    n=rri()
    res=""
    if n==1:
        print("8")
        return
    if n==2:
        print("98")
        return
    
    z=(n+4-1)//4
    res='9'*(n-z)+'8'*z
    print(res)
    return
    
# sol()
def main():
    T = rri()
    for t in range(1, T + 1):
        ans=sol()
        # print("Case #{}: {}".format(t, ans))

main()
