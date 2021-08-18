N = input()
s1 = N[1:len(N)]
s2 = N[0:len(N) - 1]
isOk = True
for i in range(1, len(N) - 1):
    if s1[i] != s1[i - 1]:
        isOk = False
        break
    else:
        continue

if isOk:
    print('Yes')
    return

isOk = True
for i in range(1, len(N) - 1):
    if s2[i] != s2[i - 1]:
        isOk = False
        break
    else:
        continue

if isOk:
    print('Yes')
else:
    print('No')
