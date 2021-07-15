n = int(input())
s = input().strip()
r = [0] * 10
for c in s:
    if c == 'L':
        for i in range(10):
            if not r[i]:
                r[i] = 1
                break
    elif c == 'R':
        for i in range(9, -1, -1):
            if not r[i]:
                r[i] = 1
                break
    else:
        r[int(c)] = 0
print(''.join(str(x) for x in r))
