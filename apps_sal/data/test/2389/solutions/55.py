def put(ret, val):
    if val == 0:
        ret.append('A')
    elif val == 1:
        ret.append('B')
    else:
        ret.append('C')


n, a, b, c = list(map(int, input().split()))

s = []

for i in range(n):
    tmp = input()
    if tmp == 'AB':
        val = 0
    elif tmp == 'BC':
        val = 1
    else:
        val = 2
    s.append(val)

ret = []
if a + b + c == 0:
    print('No')
    return
elif a + b + c == 1:
    t = []
    t.append(a)
    t.append(b)
    t.append(c)
    for i, item in enumerate(s):
        if t[item] == 1:
            t[item] = 0
            t[(item+1) % 3] = 1
            put(ret, (item+1) % 3)
        elif t[(item+1) % 3] == 1:
            t[item] = 1
            t[(item+1) % 3] = 0
            put(ret, item)
        else:
            print('No')
            return
elif a + b + c == 2:
    t = []
    t.append(a)
    t.append(b)
    t.append(c)
    for i, item in enumerate(s):
        if t[item] == 0 and t[(item+1) % 3] == 0:
            print('No')
            return
        if t[item] > t[(item+1) % 3]:
            t[item] -= 1
            t[(item+1) % 3] += 1
            put(ret, (item+1) % 3)
        elif t[item] < t[(item+1) % 3]:
            t[item] += 1
            t[(item+1) % 3] -= 1
            put(ret, item)
        elif t[item] == 0:
            print('No')
            return
        elif t[item] == 2:
            t[item] -= 1
            t[(item+1) % 3] += 1
            put(ret, (item+1) % 3)
        else:
            if len(s) > i + 1:
                if s[i+1] == (item + 1) % 3:
                    t[item] -= 1
                    t[(item+1) % 3] += 1
                    put(ret, (item+1) % 3)
                else:
                    t[item] += 1
                    t[(item+1) % 3] -= 1
                    put(ret, item)
            else:
                put(ret, item)

else:
    t = []
    t.append(a)
    t.append(b)
    t.append(c)
    for i, item in enumerate(s):
        if t[item] == 0 and t[(item+1) % 3] == 0:
            print('No')
            return
        if t[item] > t[(item+1) % 3]:
            t[item] -= 1
            t[(item+1) % 3] += 1
            put(ret, (item+1) % 3)
        else:
            t[item] += 1
            t[(item+1) % 3] -= 1
            put(ret, item)

print('Yes')
for item in ret:
    print(item)

