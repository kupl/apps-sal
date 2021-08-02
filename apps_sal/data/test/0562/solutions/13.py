import sys
n = int(input())
x = []
z = []
for i in range(n):
    a, b = map(int, input().split())
    x.append(a)
    z.append(b + 1)
x.sort()
z.sort()
s = ''
sc = 0
k = 0
j = 0
while (len(x) != k and len(z) != j):
    if x[k] > z[j]:
        s += ')'
        j += 1
    elif x[k] < z[j]:
        s += '('
        k += 1
    else:
        k += 1
        j += 1
if len(z) - j > 0:
    s += (')' * (len(z) - j))
# print(s)
for i in range(len(s)):
    if sc > 2:
        print('NO')
        return
    if s[i] == '(':
        sc += 1
    else:
        sc -= 1

print('YES')
