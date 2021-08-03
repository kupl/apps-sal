L = list(map(str, input().split()))

if L[1] == '+':
    print((int(L[0]) + int(L[2])))
else:
    print((int(L[0]) - int(L[2])))
