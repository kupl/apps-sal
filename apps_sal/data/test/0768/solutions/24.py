# :3

kitten = input("")
a = (kitten.split())
n = int(a[0])
m = int(a[1])
k = int(a[2])

ans = 0

b = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

for i in range(n):
    s = input("")
    for j in range(m):
        if s[j] == 'Y':
            b[j] = b[j] + 1

for j in range(m):
    if b[j] >= k:
        ans = ans + 1

print(ans)
