N = int(input())
glav = [0] * 2016
pob  = [0] * 2016
for i in range(N):
    x, y = map(int, input().split())
    glav[x - y] += 1
    pob[x + y] += 1
s = 0
for i in glav:
    s += i*(i - 1) // 2
for i in pob:
    s += i*(i - 1) // 2
print(s)
