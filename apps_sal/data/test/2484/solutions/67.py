n = int(input())
a = list(map(int, input().split()))

result = 0
i = 0
x = 0
for j in range(n):
    while x < n and (i & a[x]) == 0:
        i += a[x]
        x += 1
    result += x - j
    i -= a[j]
print(result)
