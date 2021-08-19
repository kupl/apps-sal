N = int(input())
a = list(input())
count = 1
for i in range(N):
    if i > 0:
        if a[i - 1] == a[i]:
            pass
        elif a[i - 1] != a[i]:
            count += 1
print(count)
