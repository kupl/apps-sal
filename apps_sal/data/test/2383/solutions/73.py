n = int(input())
A = list(map(int, input().split()))

if not 1 in A:
    print(-1)
else:
    c = 1
    for i in range(n):
        if A[i] == c:
            c += 1
    print(n - c + 1)
