n = int(input())
s = input().strip()
c = [0, 0]
for i in range(n - 1):
    if s[i] != s[i + 1]:
        if s[i] == 'S':
            c[0] += 1
        else:
            c[1] += 1
print('YES' if c[0] > c[1] else 'NO')
