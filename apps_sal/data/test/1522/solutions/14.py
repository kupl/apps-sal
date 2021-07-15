n = int(input())
line = str(input())

doors = []
keys  = []
havekeys1  = [False] * 33
havekeys2  = [0] * 33

for i in range(len(line)):
    if i % 2 == 0:
        keys.append(line[i])
    else:
        doors.append(line[i])

res = 0
for i in range(n - 1):
    havekeys1[ord(keys[i]) - 97] = True
    havekeys2[ord(keys[i]) - 97] += 1
    if havekeys1[ord(doors[i]) - 65]:
        havekeys2[ord(doors[i]) - 65] -= 1
        if havekeys2[ord(doors[i]) - 65] == 0:
            havekeys1[ord(doors[i]) - 65] = False
    else:
        res += 1

print(res)




















