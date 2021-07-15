n = int(input())
a = list(map(int, input().split()))
count = 0
i = 1
while i < len(a) - 1:
    if a[i - 1] > 3 and a[i] > 3 and a[i + 1] > 3:
        count += 1
        i += 3
    else:
        i += 1
print(count)
