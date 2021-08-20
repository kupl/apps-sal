(n, t) = map(int, input().split())
a = list(map(int, input().split()))
pos = 1
while pos < t:
    pos += a[pos - 1]
print(('NO', 'YES')[pos == t])
