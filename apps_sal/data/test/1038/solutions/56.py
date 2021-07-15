A,B=map(int,input().split())
def xo(n):
    if n%4==0:
        return n
    if n%4==1:
        return 1
    if n%4==2:
        return n+1
    return 0
print(xo(A-1)^xo(B))
