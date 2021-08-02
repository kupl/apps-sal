"""T=int(input())
for _ in range(0,T):
    n=int(input())
    a,b=map(int,input().split())
    s=input()
    s=[int(x) for x in input().split()]
    for i in range(0,len(s)):
        a,b=map(int,input().split())"""


T = int(input())
for _ in range(0, T):
    n = int(input())
    s = [int(x) for x in input().split()]
    if(len(set(s)) == 1 and s[0] == 1):
        if(len(s) % 2 == 0):
            print('Second')
        else:
            print('First')
    else:
        c = 0
        for i in range(0, len(s)):
            if(s[i] != 1):
                break
            else:
                c += 1
        if(c % 2 == 0):
            print('First')
        else:
            print('Second')
