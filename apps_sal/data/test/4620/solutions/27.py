n = int(input())
A = [0] * n
for i in range(1, n):
    (c, s, f) = map(int, input().split())
    for j in range(i):
        A[j] = max(-A[j] // f * -f, s) + c
print(*A, sep='\n')
