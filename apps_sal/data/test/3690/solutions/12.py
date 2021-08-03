def check1(h):
    nonlocal t1, t2
    if(h == t1 or h == t2):
        return -1
    if(h > min(t1, t2) and h < max(t1, t2)):
        return 1
    else:
        return 0


def check2(m):
    if(m == 5 * t1 or m == 5 * t2):
        return -1
    if(m > 5 * min(t1, t2) and m < 5 * max(t1, t2)):
        return 1
    else:
        return 0


h, m, s, t1, t2 = list(map(int, input().split()))
if(m != 0 or s != 0):
    h += 0.5
if(s != 0):
    m += 0.5
if(h > 12):
    h -= 12


l = [check1(h), check2(m), check2(s)]
for i in range(len(l) - 1, -1, -1):
    if(l[i] == -1):
        l.pop(i)
flag = 0
for val in l:
    if(val != l[0]):
        flag = 1
        break
if(flag):
    print("NO")
else:
    print("YES")
