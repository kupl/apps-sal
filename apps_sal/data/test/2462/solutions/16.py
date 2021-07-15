from sys import stdin
"""
n=int(stdin.readline().strip())
n,m=map(int,stdin.readline().strip().split())
s=list(map(int,stdin.readline().strip().split()))
"""
n=int(stdin.readline().strip())
for i in range(n):
    x=int(stdin.readline().strip())
    ans=[6,10,14]
    ans1=[6,10,15]
    sm=sum(ans)
    sm1=sm+1
    
    if x>sm and x-sm not in ans:
        print("YES")
        ans.append(x-sm)
        print(*ans)
    elif x>sm1 and x-sm1 not in ans1:
        print("YES")
        ans1.append(x-sm1)
        print(*ans1)
    else:
        print("NO")
        

