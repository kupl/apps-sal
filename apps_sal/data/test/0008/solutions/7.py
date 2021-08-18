def ism(a, b, c):
    return a == b and b == c


def isk(a, b, c):
    x = [a, b, c]
    x.sort()
    if x[0][1] == x[1][1] and x[1][1] == x[2][1]:
        if int(x[0][0]) + 1 == int(x[1][0]) and int(x[1][0]) + 1 == int(x[2][0]):
            return 1
    return 0


a, b, c = input().split()
x = [a, b, c]
typem = []
types = []
typep = []
m, s, p = 0, 0, 0

for i in x:
    if i[1] == 'm':
        m += 1
        typem.append(i)
    elif i[1] == 's':
        s += 1
        types.append(i)
    elif i[1] == 'p':
        p += 1
        typep.append(i)

ans = 0
done = 0

if isk(a, b, c) or ism(a, b, c):
    ans = 0
    done = 1

if done == 0 and a == b and b == c:
    ans = 0
    done = 1

elif done == 0 and a == b:
    ans = 1
    done = 1

elif done == 0 and b == c:
    ans = 1
    done = 1
elif done == 0 and a == c:
    ans = 1
    done = 1
if done == 0 and m >= 2:
    typem.sort()
    for i in range(len(typem) - 1):
        if abs(int(typem[i][0]) - int(typem[i + 1][0])) <= 2 and \
           abs(int(typem[i][0]) - int(typem[i + 1][0])) > 0:
            ans = 1
            done = 1

if done == 0 and s >= 2:
    types.sort()
    for i in range(len(types) - 1):
        if abs(int(types[i][0]) - int(types[i + 1][0])) <= 2 and \
           abs(int(types[i][0]) - int(types[i + 1][0])) > 0:
            ans = 1
            done = 1

if done == 0 and p >= 2:
    typep.sort()
    for i in range(len(typep) - 1):
        if abs(int(typep[i][0]) - int(typep[i + 1][0])) <= 2 and \
           abs(int(typep[i][0]) - int(typep[i + 1][0])) > 0:
            ans = 1
            done = 1

if done == 0:
    ans = 2
    done = 1

print(ans)
