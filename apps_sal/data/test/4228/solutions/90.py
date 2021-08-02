N, L = list(map(int, input().split()))
A = []
for i in range(N):
    x = L + i
    A.append(x)

y = sum(A)
B = sorted(A)

if L <= 0 and L + N - 1 >= 0:
    print(y)
elif L >= 0:
    y -= B[0]
    print(y)
elif L + N - 1 < 0:
    y -= B[N - 1]
    print(y)
