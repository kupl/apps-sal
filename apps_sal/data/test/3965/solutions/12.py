n = int(input())
a = [i for i in map(lambda x: int(x), input().split(' '))]
ss = []
for i in range(n):
    s = input()
    ss.append(s)
ok = True
for i in range(n):
    cnt = 0
    for ch in ss[i]:
        if ch in 'aeuioy':
            cnt += 1
    ok &= cnt == a[i]
if ok:
    print('YES')
else: print('NO')
