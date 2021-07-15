A, B = input().split()
A = int(A)
B = int(''.join([b for b in B if b != '.']))

print(A * B // 100)
