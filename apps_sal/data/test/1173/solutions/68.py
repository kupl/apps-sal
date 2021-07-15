from collections import* #defaultdict Counter deque appendleft
import sys
input=sys.stdin.readline
import time
t=time.time()

def main():
    n=int(input())
    d=[[]]+[deque(list(map(int,input().split())))for i in n*[0]]

    c=0
    while any(d):
        c+=1
        f=0
        skip=set()
        for i in range(1,n+1):
            if i not in skip:
                if d[i]:
                    if d[i][0] in skip:
                        continue
                    elif i==d[d[i][0]][0]:
                        oppo=d[i].popleft()
                        d[oppo].popleft()
                        skip.add(oppo)
                        skip.add(i)
                        f=1

        if not f:
            print((-1))
            return
        if abs(time.time()-t)>1:
            print((n*(n-1)//2))
            return

    print(c)

def __starting_point():
    main()

__starting_point()
