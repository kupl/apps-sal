n, k = map(int, input().split())
if k == 1:
    print(n)
else:
    bits = len(bin(n)[2:])
    print(2**bits - 1)
