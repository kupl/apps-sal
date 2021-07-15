n = int(input())

o = input()
k = [False] * 10

for c in o:
    if c.isdigit():
        k[int(c)] = 0
    elif c == 'L':
        for i in range(10):
            if not k[i]:
                k[i] = True
                break
    else:
        for i in range(9, -1, -1):
            if not k[i]:
                k[i] = True
                break
print(''.join(map(str, map(int, k))))
