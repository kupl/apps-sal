n = int(input())
x = [0] * n
y = [0] * n
for i in range(n):
    x[i], y[i] = map(int, input().split())
    if(abs(x[i]) + abs(y[i])) % 2 != (abs(x[0]) + abs(y[0])) % 2:
        print(-1)
        return
D = []
for i in reversed(range(33)):
    D.append(1 << i)
D += [1, 1]
if(abs(x[0]) + abs(y[0])) % 2 == 0:
    D.append(1)
print(len(D))
print(*D)
for i in range(n):
    X, Y = x[i], y[i]
    s = ''
    for d in D:
        if abs(X) > abs(Y):
            if X > 0:
                X -= d
                s += 'R'
            else:
                X += d
                s += 'L'
        else:
            if Y > 0:
                Y -= d
                s += 'U'
            else:
                Y += d
                s += 'D'
    print(s)
