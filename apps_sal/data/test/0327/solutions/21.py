n, k = map(int, input().split())

if k == 1:
    print(n)
else:
    print(int(bin(n)[2:].replace('0', '1'), 2))
