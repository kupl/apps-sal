n = int(input())
l = []
a = 0
s = input().split(' ')
if len(s) != n:
    while len(s) != n:
        print('Bad!')
        s = input().split(' ')
while a < len(s):
    l.append(int(s[a]))
    a += 1
count = 0
pm = 0
i = 1
if l[0] == -1:
    count += 1
else:
    i = 0
while i < len(l):
    if l[i] > 0:
        pm += l[i]
    if l[i] == -1:
        if pm > 0:
            pm -= 1
        else:
            count += 1
    i += 1
print(count)
