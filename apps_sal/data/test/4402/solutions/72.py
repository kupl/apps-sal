(A, B) = input().split()
A = int(A)
B = int(B)
if 13 <= A:
    print(B)
elif 5 < A < 13:
    print(B // 2)
else:
    print(0)
