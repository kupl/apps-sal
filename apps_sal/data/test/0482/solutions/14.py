a, b = map(int, input(). split())
A = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
if a == b:
    for i in range(a):
        print(A[i], end='')
else:
    while a >= b:
        for i in range(b):
            print(A[i], end='')
        a = a - b
    for j in range(a):
        print(A[j], end='')
