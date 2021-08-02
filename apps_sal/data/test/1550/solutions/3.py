n = int(input())
d = input()
c = d
s = '1'
m = 10**1005
for k in range(0, 11):
    for i in range(0, n):
        c = c[:i] + str((int(c[i]) + 1) % 10) + c[i + 1:]
    for i in range(0, n):
        c = c[1:] + c[0]
        b = int(c)
        if b < m:
            m = b
            s = c
print(s)
