# Codeforces 265 Div. 2
# B

n = input()
l = input().split()

x = 0
for i in range(len(l)):
    if l[i] == "1":
        x += 1
l.append("2")
c = 0
d = 0

for i in range(len(l) - 1):
    if d == 0:
        if l[i] == '1':
            c += 1
            x -= 1
            if x == 0:
                break
            if l[i + 1] == '1':
                d = 1
            else:
                c += 1
    else:
        c += 1
        x -= 1
        if x == 0:
            break
        if l[i + 1] == '0':
            c += 1
            d = 0

print(c)
