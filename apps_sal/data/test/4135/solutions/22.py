n = int(input())
a = input()
d = []
for i in range(2, n + 1):
    if n % i == 0:
        d.append(i)
for i in d:
    j = a[:i]
    j = j[::-1]
    a = j + a[i:]
print(a)
