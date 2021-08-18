def l():
    return list(map(int, input().split()))


N, X = l()
x = l()
for i in range(N):
    x[i] = abs(x[i] - X)


mini = min(x)
lst = []
for i in range(1, int(mini**0.5) + 1):
    if mini % i == 0:
        lst.append(i)
        lst.append(mini // i)

lst.sort()
lst = lst[::-1]
for i in lst:
    flag = True
    for j in x:
        if j % i != 0:
            flag = False
    if flag:
        break
print(i)
