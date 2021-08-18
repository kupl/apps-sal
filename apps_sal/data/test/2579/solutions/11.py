l, r, x, y, k = map(int, input().strip().split(' '))
u = 0
for i in range(x, y + 1):
    if(i * k <= r and i * k >= l):
        u = 1
        break
if(u == 1):
    print("YES")
else:
    print("NO")
