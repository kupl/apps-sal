x = int(input())

m = 100
i = 0
while 1:
    m += m // 100
    i += 1
    if m >= x:
        break

print(i)
