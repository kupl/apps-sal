n, m, k = map(int, input().split())
input()
s = [0] * m
for i in range(1, n):
    for j, x in enumerate(input()):
        if x == 'L':
            if j - i >= 0:
                s[j - i] += 1
        elif x == 'R':
            if j + i < m:
                s[j + i] += 1
        elif x == 'U' and i & 1 == 0:
            s[j] += 1
print(' '.join(map(str, s)))
