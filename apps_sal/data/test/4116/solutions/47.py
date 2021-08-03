n = int(input())
for i in range(1, 10):
    if (n / i <= 9) & (n % i == 0):
        print('Yes')
        break
else:
    print('No')
