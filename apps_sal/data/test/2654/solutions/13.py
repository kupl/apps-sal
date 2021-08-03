import sys
input = sys.stdin.readline
N = int(input())
AB = [tuple(map(int, input().split())) for i in range(N)]
A = []
B = []
for a, b in AB:
    A.append(a)
    B.append(b)
A.sort()
B.sort()

if N % 2 == 0:
    m = N // 2
    b = B[m] + B[m - 1]
    a = A[m] + A[m - 1]
    print(b - a + 1)
else:
    m = N // 2
    print(B[m] - A[m] + 1)
