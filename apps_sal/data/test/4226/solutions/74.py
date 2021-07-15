X,Y = (int(x) for x in input().split())
Flag = False
for A in range(0,X+1):
    B = X-A
    if 2*A+4*B==Y:
        Flag = True
        break
print(['No','Yes'][Flag])
