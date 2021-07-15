def parse(ip_address):
    a, b, c, d = [int(x) for x in ip_address.split('.')]
    return (a << 24) | (b << 16) | (c << 8) | d

n, k = [int(x) for x in input().split()]
ips = [parse(input()) for i in range(n)]
all_ones = (1 << 32) - 1
eight_ones = (1 << 8) - 1
for n_zeros in range(31, 0, -1):
    mask = all_ones << n_zeros
    if len(set(mask & ip for ip in ips)) == k:
        address = [(mask >> 24) & eight_ones, (mask >> 16) & eight_ones, (mask >> 8) & eight_ones, mask & eight_ones]
        print('.'.join(str(x) for x in address))
        return

print(-1)
