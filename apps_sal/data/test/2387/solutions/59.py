n = int(input())
s = []
for i in range(n):
    s.append(input())

ls1 = []
ls2 = []

for item in s:
    stk1 = []
    stk2 = []
    for ch in item:
        if ch == '(':
            stk2.append(ch)
        else:
            if len(stk2) > 0:
                stk2.pop()
            else:
                stk1.append(ch)
    l1 = len(stk1)
    l2 = len(stk2)
    if l2 >= l1:
        ls1.append((l1, l2))
    else:
        ls2.append((l1, l2))


ls1.sort()

cnt = 0

for item in ls1:
    cnt -= item[0]
    if cnt < 0:
        print('No')
        return
    else:
        cnt += item[1]

ls2.sort(key=lambda x: x[1])
ls2.reverse()

for item in ls2:
    cnt -= item[0]
    if cnt < 0:
        print('No')
        return
    else:
        cnt += item[1]

if cnt != 0:
    print('No')
else:
    print('Yes')

