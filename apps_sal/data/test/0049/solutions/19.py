l = []
n = []
sum = 0
multiply = 9
for i in range(1,12):
    s = '9' * i
    n.append(int(s))
    sum+=i*multiply
    multiply *= 10
    l.append(sum)
k = int(input())
if(k<9):
    print(k)
else:
    t = 0
    for i in range(len(l)):
        if(k < l[i]):
            t=i
            break
    temp = k-l[t-1]
    offset = temp%(t+1)
    value = temp//(t+1)
    number = n[t-1]+value
    if(offset == 0):
        print(number%10)
    else:
        number += 1
        offset -= 1
        print(str(number)[offset])
