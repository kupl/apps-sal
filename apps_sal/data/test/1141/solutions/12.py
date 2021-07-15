

n, m = list(map(int, input().split()))

A = input()

for _ in range(m):
    l, r, c_1, c_2 = input().split()
    l = int(l)
    r = int(r)
    for i in range(l - 1, r):
        if A[i] == c_1:
            A = A[:i] + c_2 + A[i + 1:]

print(A)

