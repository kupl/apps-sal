X = [int(x) for x in input().split()]
list.sort(X,reverse=True)
A,B,C = X[0],X[1],X[2]
count = 0

while A!=B or B!=C or C!=A:
    if (B-C)%2 == 1 and A==B:
        A=A+1
        B=B+1
        count = count + 1
    elif B!=C and (B-C)%2 == 0:
        while B!=C:
            C = C + 2
            count = count + 1
    else:
        B = B + 1
        C = C + 1
        count = count + 1

print(count)
