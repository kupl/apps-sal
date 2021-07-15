n = input().split()
k = int(n[-1])
n = int(n[0])
a = [int(x) for x in input().split()]
ii = 0
zero = list()
for x in a:
    if not x:
        zero.append(ii)
    ii += 1

if len(zero)-k <= 0:
    print(n)
    string = '1'
    for x in range(1, n):
        string += ' 1'
    print(string)
elif k == 0:
    string = ''
    for x in range(len(a)):
        string += str(a[x])
    o = ''
    while string.find(o+'1') != -1:
        o += '1'
    print(len(o))
    print(' '.join(str(x) for x in a))
else:
    maxof1 = 0
    for i in range(len(zero)-k+1):
        z = 1
        l1 = 0
        while zero[i]-z >= 0 and a[zero[i] - z]:
            l1 += 1
            z += 1
        z = 1
        l2 = 0
        while zero[i+k-1]+z <= n-1 and a[zero[i + k-1] + z]:
            l2 += 1
            z += 1
        x = zero[i + k-1] - zero[i] + 1 + l1 + l2
        if maxof1 < x:
            maxof1 = x
            maxn = i
    print(maxof1)
    for i in range(maxn, maxn+k):
        a[zero[i]] = 1
    string = str(a[0])
    for x in range(1, len(a)):
        string += ' '+str(a[x])
    print(string)
