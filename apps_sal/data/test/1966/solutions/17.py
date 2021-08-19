n = int(input())

l = []
for i in range(4):
    l.append(0)
for q in range(4):
    for i in range(1, n + 1):
        s = input()
        for j in range(1, n + 1):
            if i % 2 == j % 2 and s[j - 1] == '1':
                l[q] += 1
            if i % 2 != j % 2 and s[j - 1] == '0':
                l[q] += 1
    if q < 3:
        z = input()

# print(l)

l.sort()
n2 = n**2
count = 0
count += l[0] + l[1]
count += 2 * n2 - l[2] - l[3]

print(count)
