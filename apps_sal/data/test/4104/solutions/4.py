a = input()
(q, s) = ([0], 0)
z = []
for i in range(len(a)):
    y = a[i]
    if y == '+':
        z.append(1)
        q.append(0)
        s += 1
    elif y == '-':
        z.append(-1)
        q.append(0)
        s += 1
    q[s] = 10 * q[s] + (ord(y) - ord('0'))
otv = q[0]
for i in range(1, s + 1):
    otv += z[i - 1] * q[i]
print(otv)
