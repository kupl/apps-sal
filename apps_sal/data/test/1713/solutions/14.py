# your code goes here
rd = lambda : list(map(int,input().strip().split()))
n,s,t = rd()
A = rd()
for i in range(n):
    if s == t:
        print(i);return
    s = A[s-1]
print(-1)   

