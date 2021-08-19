n = int(input())

# a=int(input())

# n,m=map(int,input().split())

#a,b = map(int,input().split())

# a=list(map(int,input().split()))

#a=[int(input()) for i in range(n)]

#a=[[0]*n for i in range(n)]

if n % 2:
    print(0)
else:
    print(2**(n // 2))
