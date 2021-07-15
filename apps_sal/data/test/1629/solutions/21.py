n, x = list(map(int, input().split()))
a = list(map(int, input().split()))
idx = x % n
for j in range(x, x+n):
    if a[j % n] <= a[idx]:
        idx = j % n
temp = a[idx]
a[idx] += n * temp
a = [i - temp for i in a]
j = idx + 1
while j % n != x % n:
    a[j % n] -= 1
    j += 1
    a[idx] += 1
print(*a)

