done = False

a, b, c = list(map(int, input().split()))
for i in range(0, a + 1):
    if ((c - i) == (b - a + i)) and (c - i >= 0):
        print(a - i, c - i, i)
        done = True
        break

if not done:
    print('Impossible')
