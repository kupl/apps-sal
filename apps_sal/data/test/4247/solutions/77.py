n = int(input())
p = list(map(int, input().split()))
count = 0
for i in range(2, n):
    a = [p[i - 2], p[i - 1], p[i]]
    b = sorted(a)
    if a[1] == b[1]:
        count += 1
print(count)
