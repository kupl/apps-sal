n = int(input())
#x, a, b = map(int, input().split())
#l = list(map(int,input().split()))
#l = [list(map(int,input().split())) for i in range(n)]
al = []
for i in range(n):
    a = int(input())
    al.append(a)

al.insert(0, 0)
ans = -1
push = 1
for i in range(1, n+2):
    light = al[push]
    push = light
    if light == 2:
        ans = i
        break
print(ans)

