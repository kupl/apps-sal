#k = int(input())
#s = input()
#a, b = map(int, input().split())
#s, t = map(str, input().split())
#l = list(map(int, input().split()))
#l = [list(map(int,input().split())) for i in range(n)]
#a = [list(input()) for _ in range(n)]

x,a,b = list(map(int, input().split()))

if (b <= a):
    print("delicious")
elif (b <= x+a):
    print("safe")
else:
    print("dangerous")


