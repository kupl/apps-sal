starterrors = int(input())
errors1 = input()
errors2 = input()
errors3 = input()
errors = []

nowspace = -1
errors.append([])
for i in range(starterrors):
    nextspace = errors1.find(' ', nowspace + 1)
    if nextspace == -1:
        errors[0].append(int(errors1[nowspace + 1:]))
    else:
        errors[0].append(int(errors1[nowspace + 1:nextspace]))
    nowspace = nextspace

nowspace = -1
errors.append([])
for i in range(starterrors - 1):
    nextspace = errors2.find(' ', nowspace + 1)
    if nextspace == -1:
        errors[1].append(int(errors2[nowspace + 1:]))
    else:
        errors[1].append(int(errors2[nowspace + 1:nextspace]))
    nowspace = nextspace

nowspace = -1
errors.append([])
for i in range(starterrors - 2):
    nextspace = errors3.find(' ', nowspace + 1)
    if nextspace == -1:
        errors[2].append(int(errors3[nowspace + 1:]))
    else:
        errors[2].append(int(errors3[nowspace + 1:nextspace]))
    nowspace = nextspace

for i in range(3):
    errors[i].sort()

for i in range(starterrors - 1):
    if errors[0][i] != errors[1][i]:
        print(errors[0][i])
        break
    if i == starterrors - 2:
        print(errors[0][i + 1])
        break

for i in range(starterrors - 2):
    if errors[1][i] != errors[2][i]:
        print(errors[1][i])
        break
    if i == starterrors - 3:
        print(errors[1][i + 1])
        break
