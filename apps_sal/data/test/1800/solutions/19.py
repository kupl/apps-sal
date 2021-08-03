[n, m] = [int(i) for i in input().split()]
a = [int(i) for i in input().split()]
t = m * [0]
r = m * [0]
for k in range(0, m):
    [t[k], r[k]] = [int(i) for i in input().split()]

tstack = []
rstack = []
mm = -1
lastt = -1
tstack.append(t[0])
rstack.append(r[0])
top = 0
for i in range(1, m):
    while(top > -1):
        if(r[i] >= rstack[top]):
            rstack.pop()
            tstack.pop()
            top = top - 1
        else:
            break
    if(top == -1):
        rstack.append(r[i])
        tstack.append(t[i])
        top = top + 1
    else:
        if(tstack[top] != t[i]):
            rstack.append(r[i])
            tstack.append(t[i])
            top = top + 1

r0 = rstack[0]
sorteda = sorted(a[:r0])
begin = 0
end = len(sorteda) - 1

for mindex in range(0, len(tstack) - 1):
    rthis = rstack[mindex]
    rnext = rstack[mindex + 1]
    if(tstack[mindex] == 1):
        for i in range(rthis - 1, rnext - 1, -1):
            a[i] = sorteda[end]
            end = end - 1
    else:
        for i in range(rthis - 1, rnext - 1, -1):
            a[i] = sorteda[begin]
            begin = begin + 1

if(tstack[-1] == 1):
    for i in range(0, rstack[-1]):
        a[i] = sorteda[i + begin]
else:
    for i in range(0, rstack[-1]):
        a[i] = sorteda[end - i]

print(*a, sep=" ")
