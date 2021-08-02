n = int(input())
l = []
for i in range(n):
    l.append(input())
s = input()
c = "<3"
for i in range(n):
    c += l[i] + "<3"

j = 0
i = 0
lc = len(c)
ls = len(s)
found = False
while True:
    if i == lc:
        print("yes")
        break
    if j == ls:
        print("no")
        break

    if c[i] == s[j]:
        i += 1
    j += 1
