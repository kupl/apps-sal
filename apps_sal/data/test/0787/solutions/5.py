
k = int(input())
q = input()

i = 0
met = []
ts = []
while i < len(q):
    if q[i] in met:
        i += 1
    else:
        met.append(q[i])
        ts.append(i)
ts.append(len(q))

if len(ts) >= k + 1:
    print('YES')
    for i in range(len(ts) - 1):
        a = ts[i]
        b = ts[i + 1]
        if i == k - 1:
            print(q[a:])
            break
        print(q[a:b])
else:
    print('NO')


