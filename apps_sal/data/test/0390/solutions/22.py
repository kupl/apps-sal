n, a, b = map(int, input().split())
c = list(map(int, input().split()))
i, j = 0, n - 1
s = 0
t = True
while i < j:
    if c[i] != c[j] and c[i] != 2 and c[j] != 2:
        t = False
        break
    elif c[i] == 2 and c[j] == 1:
        s += b
        i += 1
        j -= 1
    elif c[i] == 1 and c[j] == 2:
        s += b
        i += 1
        j -= 1
    elif c[i] == 0 and c[j] == 2:
        s += a
        i += 1
        j -= 1
    elif c[i] == 2 and c[j] == 0:
        s += a
        i += 1
        j -= 1
    elif c[i] == 2 and c[j] == 2:
        s += 2 * min(a, b)
        i += 1
        j -= 1
    else:
        i += 1
        j -= 1
if n % 2 == 1:
    if c[n // 2] == 2:
        s += min(a, b)
if t:
    print(s)
else:
    print(-1)
