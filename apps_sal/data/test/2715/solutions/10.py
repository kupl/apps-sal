K = int(input())
r, q = divmod(K, 50)
A = [r + 49] * 50


def update():
    M = A.index(min(A))
    for i in range(50):
        if i == M:
            A[i] += 50
        else:
            A[i] -= 1


for i in range(q):
    update()
print(50)
print(*A)
