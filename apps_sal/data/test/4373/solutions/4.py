n = int(input())
a = sorted(list(map(int, input().split())))
count = 0
h = 1
for i in range(n):
    if a[i] >= h:
        h += 1
        count += 1
print(count)
