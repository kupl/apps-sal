n = int(input())

lst = []

for i in range((2 * n) - 2):
    curr = str(input())
    lst.append([i, curr])

lst.sort(key=lambda val: len(val[1]), reverse=True)

word1 = lst[0][1] + lst[1][1][-1]
word2 = lst[1][1] + lst[0][1][-1]
bool1 = True
bool2 = True

sp1 = [0 for i in range((2 * n) - 2)]
sp1[0] = 'P'
sp1[1] = 'S'
sp2 = [0 for i in range((2 * n) - 2)]
sp2[0] = 'S'
sp2[1] = 'P'

for i in range(2, (2 * n) - 2, 2):
    curr1 = lst[i][1]
    curr2 = lst[i + 1][1]
    if curr1 == word1[:n - int(i / 2) - 1] and curr2 == word1[int(i / 2) + 1:]:
        sp1[i] = 'P'
        sp1[i + 1] = 'S'
    elif curr2 == word1[:n - int(i / 2) - 1] and curr1 == word1[int(i / 2) + 1:]:
        sp1[i] = 'S'
        sp1[i + 1] = 'P'
    if curr1 == word2[:n - int(i / 2) - 1] and curr2 == word2[int(i / 2) + 1:]:
        sp2[i] = 'P'
        sp2[i + 1] = 'S'
    elif curr2 == word2[:n - int(i / 2) - 1] and curr1 == word2[int(i / 2) + 1:]:
        sp2[i] = 'S'
        sp2[i + 1] = 'P'

for i in sp1:
    if i == 0:
        bool1 = False
        break
for i in sp2:
    if i == 0:
        bool2 = False
if bool1:
    ans = ''
    newl = []
    for j in range(len(lst)):
        newl.append(lst[j] + [sp1[j]])
    newl.sort(key=lambda val: val[0])
    for j in newl:
        ans = ans + j[2]
    print(ans)
elif bool2:
    ans = ''
    newl = []
    for j in range(len(lst)):
        newl.append(lst[j] + [sp2[j]])
    newl.sort(key=lambda val: val[0])
    for j in newl:
        ans = ans + j[2]
    print(ans)
