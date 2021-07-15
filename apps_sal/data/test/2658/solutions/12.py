import bisect,collections,copy,itertools,math,string
import sys
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())
def main():
    n,k = LI()
    a = [None] + LI()
    explored = {1}
    lst = [1]
    lenth = 0
    start = 0
    junkan = []
    now = 1
    while lenth==0:
        nxt = a[now]
        if nxt in explored:
            index = lst.index(nxt)
            junkan = [lst[-1]] + lst[index:-1]
            start = index
            lenth = len(junkan)
        else:
            explored.add(nxt)
            lst.append(nxt)
        now = nxt
    ans = 0
    if k<start:
        ans = lst[k]
    else:
        r = (k-start+1)%lenth
        ans = junkan[r]

    print(ans)


main()            

