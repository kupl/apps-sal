l1 = list(input().strip())
l2 = list(input().strip())
r = 0

for i in range(len(l1) - 1):
    if l1[i] == '0' and l2[i] == '0':
        if l2[i+1] == '0':
            l1[i] = 'X'
            l2[i] = 'X'
            l2[i+1] = 'X'
            r += 1
        elif l1[i+1] == '0':
            l1[i] = 'X'
            l2[i] = 'X'
            l1[i+1] = 'X'
            r += 1
    elif l1[i] == '0':
        if l1[i+1] == '0' and l2[i+1] == '0':
            l1[i] = 'X'
            l1[i+1] = 'X'
            l2[i+1] = 'X'
            r += 1
    elif l2[i] == '0':
        if l1[i+1] == '0' and l2[i+1] == '0':
            l2[i] = 'X'
            l1[i+1] = 'X'
            l2[i+1] = 'X'
            r += 1

print(r)

