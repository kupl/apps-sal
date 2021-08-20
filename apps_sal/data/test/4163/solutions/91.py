N = int(input())
l = [list(map(int, input().split())) for l in range(N)]
k = 0
for i in range(N):
    if l[i][0] == l[i][1]:
        k += 1
    if l[i][0] != l[i][1]:
        k = 0
    if k == 3:
        print('Yes')
        break
else:
    print('No')
