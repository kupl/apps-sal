n = int(input())
N = n * n
a = [1] * (N + 1)
a[1] = 0
i = 2
while i <= N:
    if a[i] == 1:
        j = 2 * i
        while j <= N:
            a[j] = 0
            j += i
    i += 1
k = n
while a[k] == 0:
    k += 1
print(k)
for i in range(1, n + 1):
    if i < n:
        print(i, i + 1)
    if i == n:
        print(i, 1)
now = 1
for i in range(k - n):
    if now + 2 <= n:
        print(now, now + 2)
    else:
        print(now, now + 2 - n)
    if now % 2 == 1:
        now += 1
    else:
        now += 3
