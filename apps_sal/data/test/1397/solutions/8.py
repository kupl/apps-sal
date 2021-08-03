s = input().split()
n = int(s[0])
m = int(s[1])
l = []

for i in range(m):
    s = input().split()
    l.append(int(s[0]))
    l.append(int(s[1]))

l.sort()
star = 1
for x in l:
    if x == star:
        star += 1

print(n - 1)
for i in range(n):
    if i + 1 != star:
        print(str(star) + ' ' + str(i + 1))
