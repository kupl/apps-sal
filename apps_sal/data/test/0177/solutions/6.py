n = int(input())
a = ''
i = 0
while len(a) < n:
    i += 1
    a += str(i)

print(a[n - 1])
