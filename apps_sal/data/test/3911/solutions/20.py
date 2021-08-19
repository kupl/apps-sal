n = int(input())
v = []
t = 0
s = ''
while n != 0:
    s += str(n % 2)
    n //= 2
for i in range(len(s)):
    if s[i] == '1':
        v.append(i + 1)
for i in range(len(v) - 1, -1, -1):
    print(v[i], end=' ')
