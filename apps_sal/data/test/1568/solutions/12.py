from sys import stdin, stdout


def rint():
    return list(map(int, stdin.readline().split()))


(n, A, B, C, T) = rint()
t = list(rint())
D = C - B
if D < 0:
    print(n * A)
else:
    sum = A * n
    for i in range(n):
        sum += D * (T - t[i])
    print(sum)
