
n, x = list(map(int, input().split()))
l = list(map(int, input().split()))

d = 0
count = 1

for y in range(n):
    d = d + l[y]
    if d <= x:
        count += 1
    else:
        break

print(count)
