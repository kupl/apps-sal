n = int(input())
a = [*map(int, input().split())]
s = [0] * n
m = n
while m:
    for i, x in enumerate(a):
        if s[i] == 0:
            r = range(i % x, n, x)
            if all(a[j] <= x or s[j] == 'A'for j in r): s[i] = 'B'; m -= 1
            if any(a[j] > x and s[j] == 'B'for j in r): s[i] = 'A'; m -= 1
print(''.join(s))
