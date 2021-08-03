n, m = map(int, input().split())
xco, yco = {}, {}
for i in range(n):
    x, v = map(int, input().split())
    try:
        xco[x * v] += 1
    except:
        xco[x * v] = 1
for i in range(m):
    y, v = map(int, input().split())
    try:
        yco[y * v] += 1
    except:
        yco[v * y] = 1
colli = 0
for i in xco:
    if(i in yco):
        colli += min(xco[i], yco[i])
print(colli)
