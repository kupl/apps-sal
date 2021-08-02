A, B = input().split()


A = int(A)
B = int(B[:len(B) - 3] + B[len(B) - 2:])

print(int((A * B) // 100))
