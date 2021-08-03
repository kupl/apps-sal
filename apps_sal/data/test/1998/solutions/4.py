n, a, b, k = list(map(int, input().split()))
A = input()
B = A.split('1')
C = []
l = 1

for i in B:
    if len(i) >= b:
        for j in range(b - 1, len(i), b):
            C.append(j + l)
    l += len(i) + 1
C = C[:len(C) - a + 1]
print(len(C))
print(' '.join(list(map(str, C))))
