n = int(input())
a = list(map(int, input().split()))
count = 0
i = 0
while i < n and a[i] == 0:
    i += 1
while i < n:
    if a[i] == 1:
        i += 1
        count += 1
    else:
        tmp = 0
        while i < n and a[i] == 0:
            tmp += 1
            i += 1
        if i != n and tmp < 2:
            count += tmp
print(count)
