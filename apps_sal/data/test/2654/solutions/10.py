N = int(input())
AB = [list(map(int, input().split())) for _ in range(N)]
(A, B) = map(list, zip(*AB))
A.sort()
B.sort()


def median(a):
    n = N
    return a[(n + 1) // 2 - 1] if n % 2 else (a[n // 2 - 1] + a[n // 2]) / 2


A_mid = median(A)
B_mid = median(B)
r = int((B_mid - A_mid) * [2, 1][N % 2]) + 1
print(r)
