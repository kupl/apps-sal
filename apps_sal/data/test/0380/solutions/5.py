p = [0]*3
q = [0]*3

sum = 0

a1,b1 = list(map(int, input().split()))
a2,b2 = list(map(int, input().split()))
if a1 == a2:
    p[0] = 1
if b1 == b2:
    q[0] = 1
a3,b3 = list(map(int, input().split()))    
if a1 == a3:
    p[1] = 1
if b1 == b3:
    q[1] = 1
if a2 == a3:
    p[2] = 1
if b2 == b3:
    q[2] = 1

sum = 0
for i in range(3):
    sum += p[i] + q[i]

if sum == 0:
    print(3)
elif sum == 3:
    print(1)
elif sum == 2:
    print(2)
else:
    if q[1] + q[2] + q[0] == 1:
        b1 = a1
        b2 = a2
        b3 = a3
        p[0] = q[0]
        p[1] = q[1]
        p[2] = q[2]

    if p[0] == 1 and (b3 > max(b1,b2) or b3 < min(b1,b2)):
        print(2)
    elif p[1] == 1 and (b2 > max(b1,b3) or b2 < min(b1,b3)):
        print(2)
    elif p[2] == 1 and (b1 > max(b2,b3) or b1 < min(b2,b3)):
        print(2)
    else:
        print(3)
        
            














                

