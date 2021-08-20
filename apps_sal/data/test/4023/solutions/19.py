n = int(input())
b = -1
a = input().split()
(l, r) = ([], True)
for i in a:
    tmp = int(i)
    b = max(b, tmp)
    if l == [] or l[-1] > tmp:
        l.append(tmp)
    elif l[-1] == tmp:
        l.pop()
    else:
        r = False
        break
print('YES' if r and (len(l) == 0 or (len(l) == 1 and l[0] >= b)) else 'NO')
