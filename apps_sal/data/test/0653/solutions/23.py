n = int(input())
u = list(input())
d = [0] * 10
for i in range(n):
    if u[i] == 'L':
        for j in range(10):
            if d[j] == 0:
                d[j] = 1
                break
    elif u[i] == 'R':
        for j in range(9, -1, -1):
            if d[j] == 0:
                d[j] = 1
                break
    else:
        d[int(u[i])] = 0
print(''.join(map(str, d)))
