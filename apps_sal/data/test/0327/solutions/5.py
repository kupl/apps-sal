(n, k) = list(map(int, input().split()))
if k == 1:
    print(n)
else:
    bin_n = bin(n)[2:]
    max_deg = len(bin_n)
    print((1 << max_deg) - 1)
