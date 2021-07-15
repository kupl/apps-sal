l1 = [int(i) for i in input().split()]
s = [l1[1], l1[2]]
e = [l1[3], l1[4]]
wind = [c for c in input()]

beloved = ['W', 'N']

def sub(num1, num2):
    return num1 - num2

def add(num1, num2):
    return num1 + num2
op = [sub, add]
    
if s[0] < e[0]:
    beloved[0] = 'E'
    op[0] = add
if s[1] > e[1]:
    beloved[1] = 'S'
    op[1] = sub



time = 0
for w in wind:
    if s[0] == e[0] and s[1] == e[1]:
        print(time)
        return

    time += 1

    for i in (0, 1):
        if s[i] == e[i]:
            continue

        if w == beloved[i]:
            s[i] = op[i](s[i], 1)
    
if s[0] == e[0] and s[1] == e[1]:
        print(time)
        return
print(-1)
