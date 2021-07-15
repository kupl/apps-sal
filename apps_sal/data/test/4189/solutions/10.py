n = int(input())
sf = 0
hd = 0
for _ in range(n):
    _, t = input().split()
    if t == 'soft':
        sf += 1
    else:
        hd += 1
for i in range(1,20):
    if sf <= (i**2+1)//2 and hd <= (i**2+1)//2 and sf+hd<=i**2:
        print(i)
        break
