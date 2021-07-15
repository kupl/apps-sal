from sys import stdin
"""
n=int(stdin.readline().strip())
n,m=map(int,stdin.readline().strip().split())
s=list(map(int,stdin.readline().strip().split()))
s=stdin.readline().strip()
"""
T=int(stdin.readline().strip())
for caso in range(T):
    n=int(stdin.readline().strip())
    s=list(map(int,stdin.readline().strip().split()))
    s.sort()
    neg=0
    pos=0
    for i in range(n):
        if s[i]<0:
            neg+=abs(s[i])
        else:
            pos+=s[i]
    if pos==neg:
        print("NO")
    else:
        print("YES")
        if pos>neg:
            s=s[::-1]
            print(*s)
        else:
            print(*s)
            





