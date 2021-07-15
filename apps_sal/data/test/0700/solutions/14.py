def check(x, y):
    return ''.join([''.join(s) for s in x]) == ''.join([''.join(s) for s in y])

re = int(input())
a = [list(input()) for i in range(re)]
b = [list(input()) for i in range(re)]
for i in range(4):
    for j in range(2):
        if check(a, b):
            print('Yes')
            return
        b = b[::-1]
    for j in range(2):
        if check(a, b):
            print('Yes')
            return
        b = [s[::-1] for s in b]
    c = [['' for t in range(re)] for u in range(re)]
    for t in range(re):
        for u in range(re):
            c[t][u] = b[u][re - t - 1]
    b = c[:]
    if check(a, b):
        print('Yes')
        return
print('No')
