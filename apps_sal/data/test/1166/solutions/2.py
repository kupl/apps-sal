n = int(input())
l = [-1 for i in range(n + 1)]
s = input().split()
ll = [int(i) for i in s]
for i in range(n):
    j = ll[i]
    l[j] = i
res = ['.' for i in range(n + 1)]
res[n] = 'B'
for i in range(n - 1, 0, -1):
    toadd = 'B'
    pos = l[i] % i
    while pos < n:
        j = ll[pos]
        if j <= i:
            pos += i
            continue
        if abs(l[i] - l[j]) % i == 0 and res[j] == 'B':
            toadd = 'A'
            break
        pos += i
    res[i] = toadd
for i in ll:
    print(res[i], end='')
print('')
