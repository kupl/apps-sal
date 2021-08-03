n = int(input())
a = [*list(map(int, input().split()))]
b = [0] * n
s = [0] * n
m = n
while m:
    for i, x in enumerate(a):
        if s[i] == 0:
            r = list(range(i % x, n, x))
            if all(a[j] <= x or s[j] == 'A'for j in r):
                s[i] = 'B'
                m -= 1
            if any(a[j] > x and s[j] == 'B'for j in r):
                s[i] = 'A'
                m -= 1
print(''.join(s))
