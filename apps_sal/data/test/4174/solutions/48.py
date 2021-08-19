(n, x) = map(int, input().split())
a = list(map(int, input().split()))
a.append(0)
count = 0
b = 0
for i in range(n + 1):
    if b > x:
        break
    count += 1
    b += a[i]
print(count)
