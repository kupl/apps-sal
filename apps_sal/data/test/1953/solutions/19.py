x = int(input())
y = list(map(int, input().split(' ')))
y.sort()
s = 0
ct = 0
for i in range(x):
    if s <= y[i]:
        ct += 1
        s += y[i]
print(ct)
