(a, b, c) = list(map(int, input().split()))
num = c // a + 1
temp = 0
for i in range(num):
    if (c - i * a) % b == 0:
        temp = 1
        break
if temp == 1:
    print('Yes')
else:
    print('No')
