n = int(input())
s = str(input())
m = str(input())
marr = [0 for i in range(10)]
marr2 = [0 for i in range(10)]
for i in m:
    marr[int(i)] += 1
    marr2[int(i)] += 1
low = 0
high = 0
for i in s:
    i = int(i)
    b = 0
    for j in range(i, 10):
        if marr[j] > 0:
            marr[j] -= 1
            b = 1
            break
    if b == 0:
        low += 1
for i in s:
    i = int(i)
    for j in range(i + 1, 10):
        if marr2[j] > 0:
            marr2[j] -= 1
            high += 1
            break
print(low)
print(high)
