n,m=map(int,input().split())
s=input().split()
t=input().split()
q=int(input())
while q:
    y=int(input())
    print(s[(y-1)%n]+t[(y-1)%m])
    q-=1
