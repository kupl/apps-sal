import math
t = int(input())
L = [int(x) for x in input().split()]
L.sort()
ma = max(L)
S = 2 * sum(L)
Div = []

for i in range(1, int(math.sqrt(t)) + 1):
    if t % i == 0:
        Div.append(i)
        Div.append(t // i)

if len(Div) >= 2:
    if Div[-1] == Div[-2]:
        Div.pop()

Div.sort()

D = {}

for i in L:
    if i in D:
        D[i] += 1
    else:
        D[i] = 1

Candidates = []

for i in range(len(Div)):
    n = Div[i]
    m = Div[-i - 1]
    for j in range(ma, ma - m, -1):
        if D.get(j, -1) > ma - j + 1:
            break
    else:
        j -= 1
    good = ma - j
    y = 1 + (m - good) // 2
    x = m + n - ma - y
    T = x + y
    if y >= 1:
        if y <= (m + 1) // 2:
            if x <= (n + 1) // 2:
                if m * (x * (x - 1) + (n - x) * (n - x + 1)) + n * ((T - x) * (T - x - 1) + (m - T + x) * (m - T + x + 1)) == S:
                    temp = []
                    for j in range(m * n):
                        temp.append(abs(1 + (j % n) - x) + abs(1 + (j // n) - y))
                    temp.sort()
                    if temp == L:
                        print(n, m)
                        print(x, y)
                        break
else:
    print(-1)
