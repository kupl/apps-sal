(n, tim) = [int(i) for i in input().split()]
s = input()
data = []
for i in range(n):
    if s[i] == 'B':
        data.append(1)
    else:
        data.append(0)
for t in range(tim):
    i = 0
    while i < n:
        if data[i] == 1 and i + 1 < n and (data[i + 1] == 0):
            data[i] = 0
            data[i + 1] = 1
            i += 2
        else:
            i += 1
ans = ''
for i in range(n):
    if data[i] == 1:
        ans = ans + 'B'
    else:
        ans = ans + 'G'
print(ans)
