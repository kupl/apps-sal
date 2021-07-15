n, m = [int(t) for t in input().split()]

def xor(arr):
    t = 0
    for a in arr:
        t = t^a
    return t

a = []
win = False
j = 0
for i in range(n):
    tmp = [int(t) for t in input().split()]
    if len(set(tmp)) > 1:
        win = True
        j = i
    a.append(tmp)
if not win:
    if xor([t[0] for t in a]) == 0:
        print('NIE')
    else:
        print('TAK')
        print(' '.join(['1']*n))
else:
    print('TAK')
    if xor([t[0] for t in a]) != 0:
        print(' '.join(['1']*n))
    else:
        ans = ['1']*n
        k = 1
        while a[j][k] == a[j][0]:
            k += 1
        ans[j] = str(k + 1)
        print(' '.join(ans))
