n = int(input())
s = input()
r = ['0'] * 10
for i in s:
    if i == 'L':
        for j in range(10):
            if r[j] == '0':
                r[j] = '1'
                break
    elif i == 'R':
        for j in range(9, -1, -1):
            if r[j] == '0':
                r[j] = '1'
                break
    else:
        r[int(i)] = '0'
print(''.join(r))
