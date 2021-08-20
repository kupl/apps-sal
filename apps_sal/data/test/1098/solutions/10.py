n = int(input())
p = list()
for i in range(0, n):
    (g, o) = list(map(int, input().split(':')))
    p.append(g * 60 + o)
p.sort()
answ = 1440 - p[n - 1] + p[0]
for i in range(1, n):
    answ = max(answ, p[i] - p[i - 1])
k = str()
answ = answ - 1
if answ // 60 < 10:
    k = k + '0' + str(answ // 60) + ':'
else:
    k = k + str(answ // 60) + ':'
if answ % 60 < 10:
    k = k + '0' + str(answ % 60)
else:
    k = k + str(answ % 60)
print(k)
