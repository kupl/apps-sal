(n, m) = map(int, input().split())
a = [list(map(int, input().split())) for i in range(n)]
count = 0
for i in range(1, m + 1):
    check = True
    for j in range(n):
        if i not in a[j][1:]:
            check = False
    if check:
        count += 1
print(count)
