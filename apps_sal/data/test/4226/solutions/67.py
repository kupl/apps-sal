x, y = list(map(int, input().split()))

for a in range(x + 1):
    b = x - a 

    if (2 * a + 4 * b) == y:
        print('Yes')
        return

print('No')

