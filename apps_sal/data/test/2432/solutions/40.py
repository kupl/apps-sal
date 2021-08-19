n = bin(int(input()))[2:].rjust(6, '0')
print(int(n[0] + n[5] + n[3] + n[2] + n[4] + n[1], 2))
