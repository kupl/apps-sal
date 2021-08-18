
N = int(input())

D = []

for i in range(1, N + 1):
    D.append(i)


cnt = 0

for j in D:
    if j % 2 != 0:
        cnt += 1


print((cnt / len(D)))
