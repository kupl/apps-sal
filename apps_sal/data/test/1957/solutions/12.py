n, a, b = list(map(int, input().split()))
s = list(map(int, input().split()))
x = s[0]
summ = sum(s)
y = []
for i in range(n):
    y.append([s[i], i])
y.sort(reverse=True)
count = 0
index = 0
while (x * a) / summ < b:
    count += 1
    if y[index][1] == 0:
        index += 1
    summ -= y[index][0]
    index += 1
print(count)
