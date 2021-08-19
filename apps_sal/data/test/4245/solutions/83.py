(A, B) = input().split()
a = int(A)
b = int(B)
for i in range(b):
    if 1 + a * i - i >= b:
        print(i)
        break
