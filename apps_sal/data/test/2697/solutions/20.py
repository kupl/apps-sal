n = int(input())
c = 0
for i in range(1, n + 1):
    if i > 1:
        for a in range(2, i):
            if i % a == 0:
                break
        else:
            c += 1
print(c)
