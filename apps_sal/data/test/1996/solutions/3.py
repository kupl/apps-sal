s = set()
i = 'a'
while i <= 'z':
    s.add(i)
    i = chr(ord(i) + 1)
n = int(input())
c = 0
for i in range(n):
    a = input().split()
    if a[0] == '.':
        s.difference_update(set(a[1]))
    elif len(s) == 1 and i != n - 1:
        c += 1
    if a[0] == '!':
        s.intersection_update(set(a[1]))
    if a[0] == '?':
        if a[1] in s:
            s.remove(a[1])
print(c)
