x = [0, 0, 0]
y = [0, 0, 0]

def bet(a, b, c):
    return a <= c <= b or b <= c <= a

def f(i, j, k):
    return (x[k] == x[i] or x[k] == x[j]) and bet(y[i], y[j], y[k]) or (y[k] == y[i] or y[k] == y[j]) and bet(x[i], x[j], x[k])

for i in range(3):
    xi, yi = list(map(int, input().split()))
    x[i] = xi
    y[i] = yi

if (x[0] == x[1] == x[2] or y[0] == y[1] == y[2]):
    print(1)
elif f(0, 1, 2) or f(0, 2, 1) or f(1, 2, 0):
    print(2)
else:
    print(3)

