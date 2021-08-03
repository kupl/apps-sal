a, b = list(map(int, input().split()))
leg = 0
for i in range(0, a + 1):
    if 2 * i + 4 * (a - i) == b:
        print('Yes')
        return
print('No')
