n = int(input())
mas = list(map(int, input().split(' ')))
dic = {i: [0, -1, -1] for i in set(mas)}
ma = 0
for i in range(n):
    if dic[mas[i]][1] == -1:
        dic[mas[i]][1] = i
    dic[mas[i]][0] += 1
    dic[mas[i]][2] = i
    if dic[mas[i]][0] > ma:
        ma = dic[mas[i]][0]
mi = 9999999999
a = 0
b = 0
for i in range(n):
    if dic[mas[i]][0] == ma and dic[mas[i]][2] - dic[mas[i]][1] < mi:
        a = dic[mas[i]][1]
        b = dic[mas[i]][2]
        mi = b - a
print(a + 1, b + 1)
