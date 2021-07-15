p, x, y = list(map(int, input().split()))
mn = [10 ** 10]
def tr(a):
    i = (a // 50) % 475
    for j in range(25):
        i = (i * 96 + 42) % 475
        l = 26 + i
        if l == p:
            if a <= x:
                mn[0] = min(mn[0], 0)
            else:
                k = (a - x) // 50
                if k % 2 == 0:
                    mn[0] = min(mn[0], k // 2)
                else:
                    mn[0] = min(mn[0], (k + 1) // 2)
            
            
st = 0   
for i in range(50):
    if (x) % 50 == (y + i) % 50:
        st = y + i
        break
for i in range(st, 5 * 100000, 50):
    tr(i)
print(*mn)

