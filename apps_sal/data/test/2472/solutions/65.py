N = int(input())
A = [tuple(map(int, input().split())) for _ in range(N)]
A = sorted(A, key=lambda x: x[1])
c = 0
D = []
for (a, b) in A:
    c += a
    D.append(c <= b)
print('Yes' if all(D) else 'No')
