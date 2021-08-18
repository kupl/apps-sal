A = list(map(int, input().split()))
su = sum(A)

Eat = [[False] * 4 for i in range(2**4)]

for i in range(2**4):
    for j in range(4):
        if i >> j & 1:
            Eat[i][j] = True

for E in Eat:
    a1 = 0
    for i in range(4):
        if E[i]:
            a1 += A[i]
    if a1 == su - a1:
        print("Yes")
        return

print("No")
