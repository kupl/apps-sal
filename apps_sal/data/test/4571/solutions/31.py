#n=int(input())
n, m=map(int,input().split())
#l=list(map(int,input().split()))
#l=[list(map(int,input().split())) for i in range(n)]

print((1900*m+100*(n-m))*(2**m))
