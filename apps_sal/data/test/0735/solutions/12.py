n = int(input())
a = list(map(int, input().split()))
a_sort = list(a)
a_sort.sort()
index = []
for i in range(n):
    if a[i] != a_sort[i]:
        index.append(i)
if len(index) == 0:
    print('yes')
    print('1 1')
else:
    section = []
    for i in range(index[0], index[-1] + 1, 1):
        section.append(a[i])
    section_rev = [0] * len(section)
    for i in range(len(section)):
        section_rev[len(section) - 1 - i] = section[i]
    x = 0
    for i in range(index[0], index[-1] + 1):
        a[i] = section_rev[x]
        x += 1
    out = True
    for i in range(n):
        if a[i] != a_sort[i]:
            out = False
            break
    if out:
        print('yes')
        print(index[0] + 1, index[-1] + 1)
    else:
        print('no')
