n = int(input())
a = list(map(int, input().split()))
count = 0
tmp = 0

for i in range(n):
    if a[i] == tmp + 1:
        tmp = a[i]
    else:
        count += 1
print(count if count != n else -1)
