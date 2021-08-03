n = int(input())
s = input()

if n % 2 == 0:
    a = 'rb' * (n // 2)
    b = 'br' * (n // 2)
else:
    a = 'rb' * ((n - 1) // 2) + 'r'
    b = 'br' * ((n - 1) // 2) + 'b'
rr = 0
bb = 0
res = []
for i in range(n):
    if a[i] == 'r' and s[i] == 'b':
        rr += 1
        continue
    elif a[i] == 'b' and s[i] == 'r':
        bb += 1
        continue

res.append(max(rr, bb))
rr = 0
bb = 0
for i in range(n):
    if b[i] == 'r' and s[i] == 'b':
        rr += 1
        continue
    elif b[i] == 'b' and s[i] == 'r':
        bb += 1
        continue

res.append(max(rr, bb))

print(min(res))
