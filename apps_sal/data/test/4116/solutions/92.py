N = int(input())

for n in range(1, 10):
    if N % n == 0 and N // n < 10:
        print('Yes')
        break
else:
    print('No')
