
details = list(map(int,input().split()))

r = details[0]
D = details[1]
xtemp = details[2]

for i in range(0,10):
    x_next = xtemp * r - D
    print(x_next)
    xtemp = x_next


