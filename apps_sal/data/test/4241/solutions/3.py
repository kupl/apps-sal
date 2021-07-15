s = input()
t = input()
ls = []
for i in range(len(s) - len(t) + 1):
    ls.append(s[i:i+len(t)])
now = 0
minimum = len(t)
for i in range(len(ls)):
    now = 0
    for j in range(len(t)):
        if t[j] == ls[i][j]:
            now += 1
    if len(t) - now < minimum:
        minimum = len(t) - now
print(minimum)

