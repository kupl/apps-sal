n, m, k = input().split()
n = int(n)
m = int(m)
k = int(k)
array = []
for x in range(n):
    a = input().split()
    fin = []
    for i in a:
        fin.append(int(i))
    array.append(fin)
cumm = [[0 for x in range(m)] for y in range(n)]
i = 0
while(i < m):
    j = n - 1
    while(j >= 0):
        if(j == n - 1):
            cumm[j][i] = array[j][i]
        elif(array[j][i] == 1):
            cumm[j][i] = cumm[j + 1][i] + 1
        else:
            cumm[j][i] = cumm[j + 1][i]
        j -= 1
    i += 1
right = [-1 for x in range(m)]
maxm = [0 for x in range(m)]
i = 0
while(i < m):
    j = 0
    while(j < n):
        if(array[j][i] == 1):
            minm = min(k, n - j)
            if(-cumm[j + minm - 1][i] + cumm[j][i] + array[j + minm - 1][i] > maxm[i]):
                maxm[i] = -cumm[j + minm - 1][i] + cumm[j][i] + array[j + minm - 1][i]
                right[i] = j
        j += 1
    i += 1
sums = 0
for i in maxm:
    sums += i

change = 0
i = 0
while(i < len(right)):
    if(right[i] != -1):
        change += (cumm[0][i] - cumm[right[i]][i])
    i += 1
print(sums, change)
