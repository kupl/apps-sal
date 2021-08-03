a = ''
i = 1
n = int(input())
while len(a) < 10000:
    a += str(i)
    i += 1
print(a[n - 1])
