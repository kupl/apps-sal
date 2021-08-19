input = __import__('sys').stdin.readline


def MIS():
    return map(int, input().split())


(n, m) = MIS()
A = input().split()
B = input().split()
for TEST in range(int(input())):
    y = int(input()) - 1
    print(A[y % len(A)] + B[y % len(B)])
