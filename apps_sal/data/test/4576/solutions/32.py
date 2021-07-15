a = int(input())
b = int(input())
c = int(input())
g = int(input())
tmp = []
for x in range(a+1):
    for y in range(b+1):
        for z in range(c+1):
            tmp.append(500*x + 100*y + 50*z)
ans = tmp.count(g)
print(ans)
