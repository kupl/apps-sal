n = int(input())
L = []

for _ in range(n):
    s = input()
    L.append(s)

S = [(0, 1)]
k = 0

zeta = 2**32-1
fine = True

for i in range(n):
    if 'add' in L[i]:
        if (S[-1][0] == 1):
            fine = False
            break
        k += S[-1][1]
    elif 'end' in L[i]:
        S.pop()
    elif 'for' in L[i]:
        if S[-1][0] == 1:
            S.append(S[-1])
            continue
        x = int(L[i].split()[1])*S[-1][1]
        if x > zeta:
            S.append((1, 0))
        else:
            S.append((0, x))
    if k > zeta:
        fine = False
        break
if fine:
    print(k)
else:
    print('OVERFLOW!!!')



