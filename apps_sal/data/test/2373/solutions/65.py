n = int(input())
a = list(map(int, input().split()))

l = [0] * (n + 1)
for i in range(n):
    if a[i] == i + 1:
        l[i] = 1
count = 0
for i in range(n):
    if l[i] == 1:
        l[i] = 0
        l[i + 1] = 0
        count += 1
print(count)
