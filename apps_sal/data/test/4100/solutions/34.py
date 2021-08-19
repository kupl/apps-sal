(n, k, q) = map(int, input().split())
a_l = [int(input()) for _ in range(q)]
d = {}
for a in a_l:
    if a in d.keys():
        d[a] += 1
    else:
        d[a] = 1
for i in range(n):
    if i + 1 in d:
        if k - (q - d[i + 1]) > 0:
            print('Yes')
        else:
            print('No')
    elif k - q > 0:
        print('Yes')
    else:
        print('No')
