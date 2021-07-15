
t1 = [int(i) for i in input().split(':')]

A1 = 60*t1[0]+t1[1]

t2 = [int(i) for i in input().split(':')]

A2 = 60*t2[0]+t2[1]

M = (A1+A2)//2

H = M//60

M = M-(H)*60

print(str(H).zfill(2)+':'+str(M).zfill(2))


