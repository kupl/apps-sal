n = int(input())
a = [int(s) for s in input().split()]
m = int(input())
b = [int(s) for s in input().split()]
a.sort()
b.sort()
i = 0
j = 0
count = 0
while i < n and j < m:
    if abs(a[i] - b[j]) <= 1:
        count += 1
        i += 1
        j += 1
    elif a[i] < b[j]:
        i += 1
    else:
        j += 1
print(count)
