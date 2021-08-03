a, b, c = list(map(int, input().split()))
key = 0
i = 0
while (i * b <= c):
    if (c - i * b) % a == 0:
        key = 1
        break
    i += 1
if key == 0:
    print('No')
else:
    print('Yes')
