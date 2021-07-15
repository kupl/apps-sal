N,A,B = list(map(int,input().split()))
s = 0
for i in range(1,N+1):
    tmp = sum(list(map(int,str(i))))
    if A<=tmp and tmp <= B:
        s += i

print(s)
