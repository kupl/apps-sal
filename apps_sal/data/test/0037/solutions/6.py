a, b, c = list(map(int, input().split()))
for x in range(c // a + 1):
    if (c - a * x) % b == 0:
        print('Yes')
        break
else:
    print('No')

