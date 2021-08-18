S = int(input())

a = [S]
temp = S

i = 0

while i < 200:
    i += 1
    if temp % 2 == 0:
        a.append(temp // 2)
    else:
        a.append(temp * 3 + 1)
    temp = a[-1]

for n in range(200):
    for m in range(n + 1, 200):
        if a[n] == a[m]:
            print(m + 1)
            return
