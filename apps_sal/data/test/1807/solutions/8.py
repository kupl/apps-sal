def filling(i):
        if i == 0:
            return 6
        elif i == 1:
            return 2
        elif i == 2:
            return 5
        elif i == 3:
            return 5
        elif i == 4:
            return 4
        elif i == 5:
            return 5
        elif i == 6:
            return 6
        elif i == 7:
            return 3
        elif i == 8:
            return 7
        elif i == 9:
            return 6

li = []

for i in range(1000002):
    li += [-1]
for i in range(10):
    li[i] = filling(i)

def getc(i):
    s = 0
    if li[i] != -1:
        s = li[i]
    else:
        s = li[i % 10] + li[i // 10]
    li[i] = s
    return s

a, b = list(map(int, input().split()))

s = 0

for i in range(a):
    getc(i)
for i in range(a, b + 1):
    s += getc(i)

print(s)

