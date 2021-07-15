n, d = map(int, input().split())
c = 0
p = d*2 + 1
tmp = 0
while n > tmp:
    tmp = tmp+p
    c += 1
print(c)
