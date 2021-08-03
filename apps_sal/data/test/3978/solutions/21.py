n = int(input())
a = [int(i) for i in input().split()]
a.sort()
count = 0
for i in range(n):
    cur_c = a[i]
    if not cur_c:
        continue
    count += 1
    for j in range(i + 1, n):
        if a[j] % cur_c == 0:
            a[j] = 0
print(count)
