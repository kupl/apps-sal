n = int(input())
a = list(map(int, input().split()))

a_sort = list(a)
a_sort.sort()
# print(a_sort)

index = []

for i in range(n):
    if a[i] != a_sort[i]:
        index.append(i)
if len(index) == 0:
    print("yes")
    print("1 1")
else:
    section = []
    for i in range(index[0], index[-1] + 1, 1):
        section.append(a[i])
    # print(section)
    section_rev = [0] * len(section)
    # print(index)
    for i in range(len(section)):
        section_rev[len(section) - 1 - i] = section[i]
    # print(section_rev)
    x = 0
    for i in range(index[0], index[-1] + 1):
        #print(a[i], section_rev[x])
        a[i] = section_rev[x]
        x += 1
    # print(a)
    out = True
    for i in range(n):
        if a[i] != a_sort[i]:
            out = False
            break
    if out:
        print("yes")
        print(index[0] + 1, index[-1] + 1)
    else:
        print("no")
