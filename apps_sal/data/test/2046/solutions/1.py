
n = int(input())
A = list(map(int, input().split()))
V = [False] * (n + 1)
p = n
for i in range(n):
    V[A[i]] = True
    p0 = p
    while V[p]:
        print(p, end=' ')
        p -= 1
    print()
