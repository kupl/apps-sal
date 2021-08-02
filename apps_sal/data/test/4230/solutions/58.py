x, _ = list(map(int, input().split()))
p = list(map(int, input().split()))
x_l = x
x_u = x
while(True):
    if(not x_l in p):
        print(x_l)
        break
    if(not x_u in p):
        print(x_u)
        break
    x_l -= 1
    x_u += 1
