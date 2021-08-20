t = int(input())
while t > 0:
    n = int(input())
    a = input()
    b = input()
    ind = []
    for i in range(0, len(a)):
        if a[i] == b[i]:
            pass
        else:
            ind.append(i)
    if len(ind) > 2 or len(ind) == 1:
        print('No')
    elif a[ind[0]] == a[ind[1]] and b[ind[0]] == b[ind[1]]:
        print('Yes')
    else:
        print('No')
    t -= 1
