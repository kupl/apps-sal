
N = int(input())
a = list(map(int,input().split(' ')))
a.sort()
 
 
fathers = [a.pop()]
for _ in range(N):
    sons = list()
    b = list()

    for father in fathers:
        while a:
            x = a.pop()
            if father > x:
                sons.append(x)
                break
            else:
                b.append(x)
                
    a = a + b[::-1]
    fathers.extend(sons)
    fathers.sort(reverse = True)
    


if len(fathers) == 2**N:
    print('Yes')
else:
    print('No')

