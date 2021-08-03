n, k, m = map(int, input().split())
s = input().split()
x = [0] * m
for i in range(n):
    s[i] = int(s[i])
    x[s[i] % m] += 1
z = -1
for i in range(m):
    if x[i] >= k:
        z = i
        break
if z == -1:
    print('No')
else:
    i = 0
    print('Yes')
    while k > 0:
        if s[i] % m == z:
            k += -1
            print(s[i], end=' ')
        i += 1
