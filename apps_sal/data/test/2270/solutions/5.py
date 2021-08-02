import sys
input = sys.stdin.readline
n = int(input())
L = list(map(int, input().split()))
q = int(input())
ct2 = 0
ct4 = 0
ct6 = 0
ct8 = 0
ct = [0] * (10**5 + 10)
for i in L: ct[i] += 1
for i in ct:
    if i > 1: ct2 += 1
    if i > 3: ct4 += 1
    if i > 5: ct6 += 1
    if i > 7: ct8 += 1
for i in ' ' * q:
    a, b = input().split()
    b = int(b)
    if a == '+':
        ct[b] += 1
        if ct[b] == 2: ct2 += 1
        if ct[b] == 4: ct4 += 1
        if ct[b] == 6: ct6 += 1
        if ct[b] == 8: ct8 += 1
    else:
        ct[b] -= 1
        if ct[b] == 1: ct2 -= 1
        if ct[b] == 3: ct4 -= 1
        if ct[b] == 5: ct6 -= 1
        if ct[b] == 7: ct8 -= 1
    if ct2 >= 2 and ct6 >= 1: print('YES')
    elif ct2 >= 3 and ct4 >= 1: print('YES')
    elif ct4 >= 2: print('YES')
    elif ct8: print('YES')
    else: print('NO')
