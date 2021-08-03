n = int(input())
t = list(map(int, input().split()))
p = sorted(t)
a = b = 0
for i in range(n):
    if t[i] != p[i]:
        a, b = i, n - 1
        while t[b] == p[b]:
            b -= 1
        break
b += 1
print('yes\n' + str(a + 1) + ' ' + str(b) if t[a: b] == p[a: b][:: -1] else 'no')
