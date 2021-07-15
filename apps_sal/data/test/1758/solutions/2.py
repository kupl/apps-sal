n = int(input())
a = input()
b = input()
diff = 0
maxDiff = 0
minDiff = 0
for i in range(n):
    if a[i] == '1':
        diff += 1
    if b[i] == '1':
        diff -= 1
    if diff > maxDiff:
        maxDiff = diff
    if diff < minDiff:
        minDiff = diff
if diff != 0:
    print(-1)
else:
    print(maxDiff - minDiff)

