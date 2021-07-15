x = int(input())
#a, b = map(int,input().split())
#l = list(map(int,input().split()))
#l = [list(map(int,input().split())) for i in range(n)]
t = 0
c = 0

while True:
    if c >= x:
        break
    t += 1
    c += t

print(t)

