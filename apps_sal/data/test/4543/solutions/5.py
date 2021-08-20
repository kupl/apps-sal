(a, b) = input().split()
x = int(a) * 10 ** len(b) + int(b)
for i in range(0, 1000):
    if i * i == x:
        print('Yes')
        break
else:
    print('No')
