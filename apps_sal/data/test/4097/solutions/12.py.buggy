import sys


def ff(q, s):
    c = 0
    su = 1
    for i in range(1, len(q)):
        if(q[i] - q[i - 1] - s == 1):
            c += 1
            q[i] = q[i] - 1
        elif(q[i] - q[i - 1] - s == 0):
            pass
        elif(q[i] - q[i - 1] - s == -1):
            c += 1
            q[i] = q[i] + 1
        else:
            su = 0
            break
    if(su == 1):
        return c
    else:
        return -1


_ = input()
b = list(map(int, input().split()))
s = 0
for i in range(len(b) - 1):
    s += b[i + 1] - b[i]

if(len(b) == 1):
    print(0)
    return
qw = s // (len(b) - 1)
gg = []


q = b[:]
gg.append(ff(q, qw))
q = b[:]
gg.append(ff(q, qw + 1))

q = b[:]
q[0] = q[0] + 1
res = ff(q, qw)
if(res != -1):
    gg.append(res + 1)
q = b[:]
q[0] = q[0] + 1
res = ff(q, qw + 1)
if(res != -1):
    gg.append(res + 1)

q = b[:]
q[0] = q[0] - 1
res = ff(q, qw)
if(res != -1):
    gg.append(res + 1)
q = b[:]
q[0] = q[0] - 1
res = ff(q, qw + 1)
if(res != -1):
    gg.append(res + 1)

cc = []
for i in gg:
    if(i != -1):
        cc.append(i)
if(cc == []):
    print(-1)
else:
    print(min(cc))
