read = lambda: map(int, input().split())
n = int(input())
ev = []
for i in range(n):
    l, r = read()
    r += 1
    ev.append((l, 1))
    ev.append((r, -1))
ev.sort()
bal = 0
flag = 1
for x, t in ev:
    bal += t
    if bal > 2:
        flag = 0
        break
print('YES' if flag else 'NO')
