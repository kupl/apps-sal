n, m = map(int, input().split())
l = [[] for i in range(m)]
for i in range(n):
    l1 = input().split()
    team = int(l1[1]) - 1
    l[team].append([int(l1[2]), l1[0]])

for i in range(m):
    a = list(sorted(l[i]))[::-1]
    if len(a) == 2:
        print(a[0][1], a[1][1])
    elif a[1][0] == a[2][0]:
        print("?")
    else:
        print(a[0][1], a[1][1])
