(n, m) = list(map(int, input().split()))
aks = False
while n > 0 and m > 0:
    n -= 1
    m -= 1
    if aks == True:
        aks = False
    else:
        aks = True
else:
    if aks == True:
        print('Akshat')
    else:
        print('Malvika')
