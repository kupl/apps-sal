n = int(input())
x = n // 4
s = input()
a = x - s.count('A')
c = x - s.count('C')
g = x - s.count('G')
t = x - s.count('T')
L = []
if n % 4 != 0:
    print('===')
elif s.count('A') > x or s.count('C') > x or s.count('G') > x or (s.count('T') > x):
    print('===')
else:
    for i in range(a):
        L.append('A')
    for i in range(c):
        L.append('C')
    for i in range(g):
        L.append('G')
    for i in range(t):
        L.append('T')
    s1 = ''
    j = 0
    for i in s:
        if i != '?':
            s1 += i
        elif i == '?':
            s1 += L[j]
            j += 1
    if s1.count('A') + s1.count('C') + s1.count('G') + s1.count('T') != n:
        print('===')
    else:
        print(s1)
