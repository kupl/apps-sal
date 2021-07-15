#! python3

m, b = [int(x) for x in input().strip().split(' ')]

r = 0
for y in range(b+1):
    x = (b-y)*m
    p = x*(x+1)//2
    s = p * (y+1) + x * y * (y+1) // 2 + y * (y+1) // 2
    if s > r:
        #print(y)
        r = s
print(r)

