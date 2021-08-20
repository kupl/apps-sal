n = int(input())
a = n
m = 0
for i in range(n + 1):
    j = 1
    for h in range(i + 1):
        if i % 2 ** j != 0:
            if m < j - 1:
                m = j - 1
                a = i
            break
        j += 1
print(a)
