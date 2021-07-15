a = int(input())

bin_a = bin(a)[2:]
bin_a = (6 - len(bin_a)) * '0' + bin_a

result = bin_a[0] + bin_a[5] + bin_a[3] + bin_a[2] + bin_a[4] + bin_a[1]
print(int(result, 2))
