a = [[*map(int, input().split())] for _ in range(3)]
b = [int(input()) for _ in range(int(input()))]
for i in b:
    for j in range(3):
        if i in a[j]:
            a[j][a[j].index(i)] = -1
if a[0][0] + a[1][1] + a[2][2] == -3 or a[0][2] + a[1][1] + a[2][0] == -3:
    print('Yes')
else:
    for i, j in zip(a, [*zip(*a)]):
        if sum(i) == -3 or sum(j) == -3:
            print('Yes')
            break
    else:
        print('No')
