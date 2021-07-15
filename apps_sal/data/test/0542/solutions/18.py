n = int(input())
a1 = []
a2 = []
last = True
for i in range(n):
    v = int(input())
    if v > 0:
        a1.append(v)
    else:
        a2.append(-v)
    if i == n - 1:
        last = v > 0
s1 = sum(a1)
s2 = sum(a2)
if s1 > s2 or (s1 == s2 and a1 > a2) or (s1 == s2 and a1 == a2 and last):
    print('first')
else: 
    print('second')

