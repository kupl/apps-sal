n = int(input())
a = list(map(int, input().split()))
b = a[:]
for i in range(n):
    b[i] = a[i] - a[i] % n + i
    if b[i] < a[i]:
        b[i] += n
mn = 0
for i in range(n):
    if b[mn] > b[i]:
        mn = i
print(mn + 1)
