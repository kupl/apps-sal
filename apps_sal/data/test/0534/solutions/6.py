
n, t = map(int, input().split())
a = list(input())

for i in range(t):
    j = 0
    while j < n:
        while j < n and a[j] == 'G':
            j += 1
        while j < n and a[j] == 'B':
            j += 1
        if j < n:
            a[j - 1], a[j] = 'G', 'B'
            j += 1

for i in a:
    print(i, end='')
