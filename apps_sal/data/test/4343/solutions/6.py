n = int(input())
s = input()
t = input()
dic = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

slis = []
tlis = []
for i in s:
    slis.append(dic.index(i))
for i in t:
    tlis.append(dic.index(i))

sumlis = []
cout = 0
for j in range(n - 1, -1, -1):
    res = slis[j] + tlis[j] + cout
    if j != 0:
        if res >= 26:
            res = res % 26
            cout = 1
        else:
            cout = 0
    sumlis.append(res)

total = sumlis[::-1]

for i in range(n):
    if total[i] % 2 == 1:
        total[i] //= 2
        total[i + 1] += 26
    else:
        total[i] //= 2

result = []

for i in total:
    result.append(dic[i])

print("".join(result))
