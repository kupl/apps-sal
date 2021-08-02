N = int(input())
A = list(map(int, input().split()))
mi, ma = min(A), max(A)
print(2 * N)
if abs(mi) <= ma:
    k = A.index(ma)
    print(k + 1, 1)
    print(k + 1, 1)
    for i in range(N - 1):
        print(i + 1, i + 2)
        print(i + 1, i + 2)
else:
    k = A.index(mi)
    print(k + 1, N)
    print(k + 1, N)
    for i in reversed(range(N - 1)):
        print(i + 2, i + 1)
        print(i + 2, i + 1)
