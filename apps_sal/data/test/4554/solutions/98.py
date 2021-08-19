#k = int(input())
#s = input()
#a, b = map(int, input().split())
#s, t = map(str, input().split())
#l = list(map(int, input().split()))
#l = [list(map(int,input().split())) for i in range(n)]
#a = [list(input()) for _ in range(n)]


W, a, b = list(map(int, input().split()))

if (b + W < a):
    print((a - (b + W)))
elif (a + W < b):
    print((b - (a + W)))
else:
    print((0))
