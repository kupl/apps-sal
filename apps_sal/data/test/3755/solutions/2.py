N = int(input())
A = list(map(int, input().split()))
data = [[], []]
flag = [[], []]
for i in range(N):
    data[i % 2].append(A[i])
    flag[0].append(i % 2)
    flag[1].append((i + 1) % 2)
num0 = 0
for i in range(len(data[0])):
    u = data[0][i]
    if u > 0:
        num0 += u
    else:
        flag[0][2 * i] = 1
if num0 == 0:
    num0 = max(data[0])
    flag[0] = [1 for i in range(N)]
    for i in range(len(data[0])):
        u = data[0][i]
        if u == num0:
            flag[0][2 * i] = 0
            break
num1 = 0
for i in range(len(data[1])):
    u = data[1][i]
    if u > 0:
        num1 += u
    else:
        flag[1][2 * i + 1] = 1
if num1 == 0:
    num1 = max(data[1])
    flag[1] = [1 for i in range(N)]
    for i in range(len(data[1])):
        u = data[1][i]
        if u == num1:
            flag[1][2 * i + 1] = 0
            break
if num0 > num1:
    print(num0)
    H = flag[0]
else:
    print(num1)
    H = flag[1]
ans = []
ddd = 0
for i in range(N):
    if H[i] == 1:
        ans.append(1)
        ddd += 1
    else:
        H = H[i:]
        break
H = [0] + H
kkk = N - ddd
while True:
    if H[kkk] == 1:
        ans.append(kkk)
        kkk -= 1
    else:
        break
while kkk > 0:
    if H[kkk] == 0:
        kkk -= 1
    else:
        cnt = 0
        while H[kkk] == 1:
            kkk -= 1
            cnt += 1
        for j in range((cnt + 1) // 2, 0, -1):
            ans.append(kkk + j)
print(len(ans))
for u in ans:
    print(u)
