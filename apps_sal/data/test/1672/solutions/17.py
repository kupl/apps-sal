n = int(input())
count = 1
a = []
for i in range(n):
    a.append(int(input()))
for i in range(1, n):
    if a[i] != a[i - 1]:
        count += 1
print(count)
