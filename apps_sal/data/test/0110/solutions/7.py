n = int(input())
a = list(map(int, input().split()))

max_mod = 0
max_i = -1
for i in range(n):
    if a[i] >= 0:
        a[i] = -a[i] - 1
    if -a[i] > max_mod:
        max_mod = -a[i]
        max_i = i

if n % 2 == 1:
    a[max_i] = -a[max_i] - 1

print(' '.join(list(map(str, a))))
