n = int(input())
list1 = list(map(int, input().strip().split(' ')))
m = int(input())
s = sum(list1)
list2 = []
for i in range(m):
    a, b = input().strip().split(' ')
    a, b = (int(a), int(b))
    list2.append((a, b))
if m == 0:
    print(-1)
    return
if s > list2[-1][1]:
    print(-1)
    return
else:
    for j in range(m):
        if (list2[j][1] >= s):
            print(max(list2[j][0], s))
            return
