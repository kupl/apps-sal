(x, y, a, b, c) = map(int, input().split())
p = list(map(int, input().split()))
q = list(map(int, input().split()))
r = list(map(int, input().split()))
s = []
for i in range(a):
    s.append([p[i], 1])
for i in range(b):
    s.append([q[i], 2])
for i in range(c):
    s.append([r[i], 0])
s.sort(reverse=True)
o = 0
(X, Y, Z) = (0, 0, 0)
for i in range(a + b + c):
    if s[i][1] == 1 and X < x:
        X += 1
        Z += 1
        o += s[i][0]
    elif s[i][1] == 2 and Y < y:
        Y += 1
        Z += 1
        o += s[i][0]
    elif s[i][1] == 0:
        Z += 1
        o += s[i][0]
    if Z == x + y:
        break
print(o)
