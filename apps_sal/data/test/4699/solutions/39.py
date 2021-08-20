(N, K) = map(int, input().split())
D = list(map(int, input().split()))
E = []
for i in range(10):
    if i not in D:
        E.append(i)
E = sorted(E)
N = str(N)
ind = len(N)
for i in range(len(N)):
    if int(N[i]) not in E:
        ind = i
        break
if ind == len(N):
    print(N)
else:
    flag = 0
    x = ''
    for i in range(ind, -1, -1):
        n = int(N[i])
        for e in E:
            if e > n:
                x = N[:i] + str(e) + str(E[0]) * (len(N) - i - 1)
                flag = 1
                break
        if flag == 1:
            break
    if flag == 0:
        if E[0] > 0:
            a = E[0]
        else:
            a = E[1]
        x = str(a) + str(E[0]) * len(N)
    print(x)
