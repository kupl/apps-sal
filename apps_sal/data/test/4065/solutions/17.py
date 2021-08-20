n = int(input())
l = list(map(int, input().strip().split()))
le = 1
lm = 0
prev = l[0]
for i in range(1, n):
    if l[i] <= prev * 2:
        le = le + 1
        prev = l[i]
    else:
        if le > lm:
            lm = le
        le = 1
        prev = l[i]
if le > lm:
    lm = le
print(lm)
