n = int(input())
a = int(n / 7)
for i in range(a, -1, -1):
    if (n - 7 * i) % 4 == 0:
        print('Yes')
        return
print('No')
