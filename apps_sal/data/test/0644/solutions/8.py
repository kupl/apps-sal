# tzuyu <3

N = pow(2, 32)

l = int(input())
n = 0
s = []
t = []
for _ in range(l):
    i = input()
    if i == 'add':
        if t:
            t[-1] += 1
        else:
            n += 1
            if n >= N:
                import sys
                print('OVERFLOW!!!')
                return
    if i.startswith('for'):
        i = i.split(' ')
        c = int(i[1])
        s.append(c)
        t.append(0)
    if i == 'end':
        c = s.pop()
        x = t.pop()
        x *= c
        if t:
            t[-1] += x
            if t[-1] >= N:
                import sys
                print('OVERFLOW!!!')
                return
        else:
            n += x
            if n >= N:
                import sys
                print('OVERFLOW!!!')
                return

if n >= N:
    import sys
    print('OVERFLOW!!!')
    return
print(n)

