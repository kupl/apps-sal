import sys,math,collections,itertools
input = sys.stdin.readline

N,K=list(map(int,input().split()))
m=10**9+7

def arrange(red,blue,m):
    if red+1<blue:
        return 0
    a = (math.factorial(red+1))%m
    b = pow(math.factorial(blue),m-2,m)
    c = pow(math.factorial(red+1-blue),m-2,m)

    return (a*b*c)%m

def bluegroup(blue,group,m):
    a = (math.factorial(blue-1))%m
    b = pow(math.factorial(group-1),m-2,m)
    c = pow(math.factorial(blue-group),m-2,m)

    return (a*b*c)%m

for i in range(1,K+1):
    print(((arrange(N-K,i,m)*bluegroup(K,i,m))%m))

