(a, b) = map(int, input().split())
print(2 ** (a ^ b).bit_length() - 1)
