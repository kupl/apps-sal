import math
(N, K) = map(int, input().split())
data = [list(map(int, input().split())) for i in range(N)]
ans1 = []
for i in range(N - 1):
    for j in range(i + 1, N):
        m = 0
        for k in range(N):
            if data[i][k] + data[j][k] > K:
                m += 1
                break
        if m == 0:
            ans1.append([i, j])
ans2 = []
for i in range(N - 1):
    for j in range(i + 1, N):
        m = 0
        for k in range(N):
            if data[k][i] + data[k][j] > K:
                m += 1
                break
        if m == 0:
            ans2.append([i, j])
li1 = [[] for i in range(N)]
for i in range(len(ans1)):
    li1[ans1[i][0]].append(ans1[i][1])
    li1[ans1[i][1]].append(ans1[i][0])
L1 = [-1] * N
for i in range(N):
    if L1[i] != -1:
        continue
    L1[i] = i
    deque = [i]
    while deque:
        x = deque.pop(0)
        for j in li1[x]:
            if L1[j] == -1:
                L1[j] = i
                deque.append(j)
num1 = 1
l1 = list(set(L1))
for i in l1:
    num1 *= int(math.factorial(L1.count(i)))
    num1 = num1 % 998244353
li2 = [[] for i in range(N)]
for i in range(len(ans2)):
    li2[ans2[i][0]].append(ans2[i][1])
    li2[ans2[i][1]].append(ans2[i][0])
L2 = [-1] * N
for i in range(N):
    if L2[i] != -1:
        continue
    L2[i] = i
    deque = [i]
    while deque:
        x = deque.pop(0)
        for j in li2[x]:
            if L2[j] == -1:
                L2[j] = i
                deque.append(j)
num2 = 1
l2 = list(set(L2))
for i in l2:
    num2 *= int(math.factorial(L2.count(i)))
    num2 = num2 % 998244353
print(num1 * num2 % 998244353)
