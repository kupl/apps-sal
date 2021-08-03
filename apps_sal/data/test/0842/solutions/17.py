n = input()
print(n, end='')
l = len(n)
for i in range(l - 1, -1, -1):
    print(n[i], end='')
