k = int(input())
X, Y = map(int, input().split())
x = max(abs(X), abs(Y))
y = min(abs(X), abs(Y))
c = (k - (x + y) % k) % k
if k % 2 == 0 and (x + y) % 2 == 1:
    print(-1)
    return

a = []
m = ((x + y - 1) // k + 1)
if x + y < k:
    if (x + y) % 2 == 1:
        a.append((x, x - k))
        a.append((x + (k + x - y) // 2, (-k + x + y) // 2))
    else:
        a.append(((x + y) // 2, -k + (x + y) // 2))

if c % 2 == 1 and x + y >= k:
    m += 1
A = abs((k * m - x - y) // 2)
for i in range(m - 1):
    l = k * i + k
    if A >= l:
        a.append((0, -1))
    elif A < l <= x + A:
        a.append((l - A, -A))
    elif x + A < l:
        a.append((x, l - x - 2 * A))

a.append((x, y))
print(len(a))
for i, j in a:
    if abs(X) < abs(Y):
        i, j = j, i
    if X < 0:
        i *= -1
    if Y < 0:
        j *= -1
    print(i, j)
