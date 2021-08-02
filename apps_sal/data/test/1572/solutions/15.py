n = int(input())
a = [int(i) for i in input().split()]
b = [False, False]
for i in range(2, n):
    if a[i] == a[i - 1] + a[i - 2]:
        b.append(True)
    else:
        b.append(False)
max = 0
now = 0
for i in b:
    if i:
        now += 1
    else:
        if now > max:
            max = now
        now = 0;
if now > max:
    max = now
print(min(n, max + 2))
