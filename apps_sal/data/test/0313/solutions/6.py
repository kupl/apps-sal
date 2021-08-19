n = int(input())
s = input()
a = s.split(' ')
a = [int(i) for i in a]
c = 0
r = 0
for i in range(n):
    if i == n - 1:
        if a[i] == 1:
            c += 1
    elif r > 0:
        if a[i] == 0 and a[i + 1] == 0:
            r = 0
        else:
            c += 1
    elif a[i] == 1:
        c += 1
        r = 1
print(c)
