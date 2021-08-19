n = int(input())
m = 0
i = 0
while 2 ** i <= n:
    m = max(m, 2 ** i)
    i += 1
print(m)
