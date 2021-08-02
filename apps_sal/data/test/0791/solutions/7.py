w = int(input())
x = int(input()[::-1], 2)
y = (x + 1) % 2**w
print(bin(y ^ x).count("1"))
