def sum_n(n):
    l = len(n)

    summ = 0
    for i in range(l):
        summ += int(n[i])

    return summ

def transfer(x, i):
    x = list(x)
    
    x[i+1] = '9'
    if x[i] != '0':
        x[i] = str(int(x[i])-1)
    else:
        j = i
        while (j > 0) and (int(x[j]) == 0):
            x[j] = '9'
            j -= 1
        x[j] = str(int(x[j])-1)
    if (x[0] == '0'):
        del x[0]

    return x

x = list(input())
max_cifr = sum_n(x)
maxnum = x
res = ''

for i in range(len(x)-2, -1, -1):
    x = transfer(x, i)
    if(max_cifr < sum_n(x)):
        max_cifr = sum_n(x)
        maxnum = x

for i in range(len(maxnum)):
    res = res+maxnum[i]
    
print(res)

