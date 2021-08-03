n, k = list(map(int, input().split()))

for i in range(1, min(k + 1, 10000000)):
    if n % i != i - 1:
        print('No')
        break
else:
    print('Yes')
