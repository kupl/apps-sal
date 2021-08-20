from sys import stdin
n = int(stdin.readline().rstrip())
a = [0] * n
for x in range(n):
    a[x] = int(stdin.readline().rstrip())
a.sort(reverse=True)
sum = 1
for x in range(n - 1):
    if a[x] > a[x + 1]:
        sum += 1
print(sum)
