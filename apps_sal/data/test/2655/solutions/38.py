a = input()
N = int(a)
A = list(map(int, input().split()))
A.sort()
x = A[N - 1]
for i in range(1, (N - 2) // 2 + 1):
    x = x + 2 * A[N - 1 - i]
if (N - 2) % 2 == 1:
    x = x + A[N - 2 - (N - 2) // 2]
print(x)
