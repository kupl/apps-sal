a, b, c = map(int, input().split())
possible = False
for i in range(c//a + 1):
    if (c - a*i) % b == 0:
        possible = True
if possible:
    print('Yes')
else:
    print('No')
