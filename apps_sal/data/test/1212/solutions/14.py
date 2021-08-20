(n, k) = input().split()
n = int(n)
k = int(k)
f = [int(x) for x in input().split()]
tmp = 0
for i in range(k):
    tmp += f[i]
mini = tmp
pos = 0
for i in range(k, n):
    tmp += f[i] - f[i - k]
    if tmp < mini:
        mini = tmp
        pos = i - k + 1
print(pos + 1)
