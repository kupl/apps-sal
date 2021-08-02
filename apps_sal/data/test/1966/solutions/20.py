N = int(input())
a = [0, 1] * N
a2 = [1, 0] * N
pt1 = []
pt2 = []

cnt = 0
for j in range(N):
    arr = input()
    for k in range(N):
        if j % 2 == 1 and int(arr[k]) == a2[k]:
            cnt += 1

        elif j % 2 == 0 and int(arr[k]) == a[k]:
            cnt += 1


pt1.append(cnt)
pt2.append(N * N - cnt)


cnt = 0
s = input()
for j in range(N):
    arr = input()
    for k in range(N):
        if j % 2 == 1 and int(arr[k]) == a2[k]:
            cnt += 1

        elif j % 2 == 0 and int(arr[k]) == a[k]:
            cnt += 1

pt1.append(cnt)
pt2.append(N * N - cnt)
s = input()
cnt = 0
for j in range(N):
    arr = input()
    for k in range(N):
        if j % 2 == 1 and int(arr[k]) == a2[k]:
            cnt += 1

        elif j % 2 == 0 and int(arr[k]) == a[k]:
            cnt += 1

pt1.append(cnt)
pt2.append(N * N - cnt)

s = input()

cnt = 0
for j in range(N):
    arr = input()
    for k in range(N):
        if j % 2 == 1 and int(arr[k]) == a2[k]:
            cnt += 1

        elif j % 2 == 0 and int(arr[k]) == a[k]:
            cnt += 1

pt1.append(cnt)
pt2.append(N * N - cnt)

pt1.sort()
pt2.sort()
print(pt1[0] + pt1[1] + pt2[0] + pt2[1])
