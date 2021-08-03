a = set('abcdefghijklmnopqrstuvwxyz')
n = int(input())
for i in range(n):
    e, b = input().split()
    if e == '!':
        a.intersection_update(set(b))
    elif e == '?' and (i != (n - 1)):
        a.difference_update(set(b))
    elif e == '.':
        a.difference_update(set(b))
    if len(a) == 1:
        break
s = 0
for j in range(i + 1, n):
    e, b = input().split()
    if e == '!' or (e == '?' and j != (n - 1)):
        s += 1
print(s)
