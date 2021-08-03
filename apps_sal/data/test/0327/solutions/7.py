n, k = list(map(int, input().split()))

if k == 1:
    print(n)
else:
    print(int('1' * len(bin(n)[2:]), 2))
