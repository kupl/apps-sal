idx = [0, 5, 3, 2, 4, 1]
n = int(input())
b = bin(n)[2:]
b = '0'*(6 - len(b)) + b
output_str = ''.join([b[i] for i in idx])
print(int(output_str, 2))

