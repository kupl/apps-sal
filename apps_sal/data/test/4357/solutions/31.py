#k = int(input())
#s = input()
#a, b = map(int, input().split())
#s, t = map(str, input().split())
#l = list(map(int, input().split()))
#l = [list(map(int,input().split())) for i in range(n)]
#a = [list(input()) for _ in range(n)]
#a = [input() for _ in range(n)]

l = list(map(int, input().split()))

l.sort()
print((l[2]*10+l[1]+l[0]))



