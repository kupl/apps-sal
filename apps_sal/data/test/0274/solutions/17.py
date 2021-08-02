n = int(input())
s = input()
bal = 0
m = 0
v = [0] * n
for i in range(n):
    if s[i] == '[':
        bal += 1
        v[i] = bal
        m = max(m, bal)
    else:
        v[i] = -bal
        bal -= 1
for j in range(1, 2 * m + 2):
    for i in range(0, n):
        if abs(v[i]) == j or abs(v[i]) == 2 * (m + 1) - j:
            if v[i] > 0:
                print('+-', end='')
            else:
                print('-+', end='')
        elif abs(v[i]) < j and abs(v[i]) < 2 * (m + 1) - j:
            print('|', end='')
            if i + 1 < n and v[i + 1] < 0 and v[i] == -v[i + 1]:
                print('  ', end='')
        else:
            print(' ', end='')
            if i > 0 and abs(v[i - 1]) >= abs(v[i]) and i + 1 < n and abs(v[i + 1]) >= abs(v[i]):
                print(' ', end='')
        if i + 1 < n and v[i + 1] < 0 and v[i] == -v[i + 1]:
            print(' ', end='')
    print()
