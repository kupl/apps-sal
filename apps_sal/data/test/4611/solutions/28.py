N = int(input())
A = [[0, 0, 0]]
for i in range(N):
    A.append(list(map(int, input().split())))
flag = True
for i in range(N):
    if not flag:
        break
    time = int(A[i + 1][0]) - int(A[i][0])
    dist = abs(A[i + 1][1] - A[i][1]) + abs(A[i + 1][2] - A[i][2])
    if time < dist:
        flag = False
    elif time % 2 != dist % 2:
        flag = False
if flag:
    print('Yes')
else:
    print('No')
