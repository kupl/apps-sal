#n = int(input())
a, b = list(map(int, input().split()))
#l = list(map(int,input().split()))
#l = [list(map(int,input().split())) for i in range(n)]
v = (a+b)//2
mod = (a+b) % 2
if mod == 0:
    print(v)
else:
    print((v+1))

