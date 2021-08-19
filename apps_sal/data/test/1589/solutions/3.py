(n, m) = [int(s) for s in input().split()]
c = 0
for j in range(n):
    s = input().split()
    for i in range(0, 2 * m, 2):
        if s[i] == '1' or s[i + 1] == '1':
            c += 1
print(c)
