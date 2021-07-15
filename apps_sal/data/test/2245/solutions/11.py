
from sys import stdin
c=int(stdin.readline().strip())
for i in range(c):
    n,m=list(map(int,stdin.readline().strip().split()))
    if n==0:
        print("Bob")
        continue

    if m%3==0:
        n=n%(m+1)
        if (n==0 or n%3==0) and  n!=m:
            print("Bob")
        else:
            print("Alice")
        continue
    if n%3==0:
        print("Bob")
    else:
        print("Alice")
"""
k=6
dp=["B","A","A"]
for i in range(3,30):
    n=len(dp)
    if n-k>=0:
        if dp[n-1]=="B" or dp[n-2]=="B" or dp[n-k]=="B":
            dp.append("A")
            continue
        else:
            dp.append("B")
            continue
    else:
        if dp[n-1]=="B" or dp[n-2]=="B":
            dp.append("A")
            continue
        else:
            dp.append("B")
            continue  
        
"""

