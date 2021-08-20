n = int(input())
l = list(map(int, input().split()))
v = list(map(int, input().split()))
d = dict()
for i in range(n):
    take = []
    for j in range(i + 1, n):
        if l[i] < l[j]:
            take.append(v[j])
    d[i] = sorted(take)
mini = 99999999999
for i in range(n):
    sum1 = v[i]
    for j in range(i + 1, n):
        if l[i] < l[j]:
            sum1 = v[j] + v[i]
            if len(d[j]) != 0:
                sum1 = v[i] + v[j] + d[j][0]
                if mini > sum1:
                    mini = sum1
if mini == 99999999999:
    print('-1')
else:
    print(mini)
