seq = bin(int(input()))[2:].rjust(6, '0')
print(int(seq[0] + seq[5] + seq[3] + seq[2] + seq[4] + seq[1], 2))
