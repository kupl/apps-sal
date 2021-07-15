#81B
N=int(input())
data=map(int,input().split())
def wareru(n):
    p=0
    while n%2==0:
        n=n//2
        p=p+1
    return p
print(min(map(wareru,data)))
