#k = int(input())
#s = input()
#a, b = map(int, input().split())
#s, t = map(str, input().split())
#l = list(map(int, input().split()))
#l = [list(map(int,input().split())) for i in range(n)]
#a = [list(input()) for _ in range(n)]
#a = [input() for _ in range(n)]

n = int(input())

q, mod = divmod(n,111)

if mod == 0:
    print((q*111))
else:
    print(((q+1)*111))


