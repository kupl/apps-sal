a, b, c, x, y = map(int, input().split(' '))

c = int(c*2)
m = float('inf')
for i in range(10**5+1):
    m = min(m, a*max(0, x-i)+b*max(0,y-i)+c*i)
print(m)
