from statistics import median
N = int(input())
A = []
B = []
for n in range(N):
    a, b = map(int, input().split())
    A.append(a)
    B.append(b)
cenA = median(A)
cenB = median(B)


if N % 2 == 1:
    print(int(cenB - cenA + 1))

elif N % 2 == 0:
    print(int((cenB - cenA) * 2 + 1))

else:
    print('RE')
