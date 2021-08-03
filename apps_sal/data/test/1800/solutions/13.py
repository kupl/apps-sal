[n, m] = [int(i) for i in input().split()]
a = [int(i) for i in input().split()]
t = m * [0]
r = m * [0]
for k in range(0, m):
    [t[k], r[k]] = [int(i) for i in input().split()]

tt = []
rr = []
mm = -1
lastt = -1
tt.append(t[0])
rr.append(r[0])
top = 0
for i in range(1, m):
    while(top > -1):
        if(r[i] >= rr[top]):
            rr.pop()
            tt.pop()
            top = top - 1
        else:
            break
    if(top == -1):
        rr.append(r[i])
        tt.append(t[i])
        top = top + 1
    else:
        if(tt[top] != t[i]):
            rr.append(r[i])
            tt.append(t[i])
            top = top + 1

r0 = rr[0]
sorteda = sorted(a[:r0])
b = 0
end = len(sorteda) - 1

for mindex in range(0, len(tt) - 1):
    rthis = rr[mindex]
    rnext = rr[mindex + 1]
    if(tt[mindex] == 1):
        for i in range(rthis - 1, rnext - 1, -1):
            a[i] = sorteda[end]
            end = end - 1
    else:
        for i in range(rthis - 1, rnext - 1, -1):
            a[i] = sorteda[b]
            b = b + 1

if(tt[-1] == 1):
    for i in range(0, rr[-1]):
        a[i] = sorteda[i + b]
else:
    for i in range(0, rr[-1]):
        a[i] = sorteda[end - i]

print(*a, sep=" ")
