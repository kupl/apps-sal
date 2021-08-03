n, b = input().split()
n = int(n)
b = int(b)
a = [int(x) for x in input().split()]
odd = 0
not_odd = 0
pos = list()
for i in range(n - 1):
    if a[i] % 2 == 0:
        not_odd += 1
    else:
        odd += 1
    if not_odd == odd:
        pos.append(abs(a[i + 1] - a[i]))
pos.sort()
sum = 0
count = 0
for i in range(len(pos)):
    if sum + pos[i] <= b:
        sum += pos[i]
        count += 1
print(count)
