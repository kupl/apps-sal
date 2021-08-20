(a, b) = input().split()
ab = int(a + b)
i = 0
while i ** 2 <= ab:
    flag = i ** 2 == ab
    i = i + 1
if flag:
    print('Yes')
else:
    print('No')
