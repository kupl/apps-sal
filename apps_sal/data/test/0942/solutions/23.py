n = int(input())
L = [n - int(x) for x in input().split()]
D = {}
for i in L:
    if i in D:
        D[i] += 1
    else:
        D[i] = 1
s = 0
check = True
for i in D.keys():
    if D[i] % i != 0:
        check = False
        break
    else:
        s += D[i]
if s != n:
    print('Impossible')

else:
    if check == False:
        print('Impossible')
    else:
        print('Possible')
        small = 1
        D2 = {}
        for i in D:
            D2[i] = list(range(small, small + (D[i] // i))) * i
            small += D[i] // i
        for i in L:
            print(D2[i][-1], end=' ')
            D2[i].pop()
