n = int(input())
X = 10 ** 18

for i in range(X):
    if 3 ** i > X:
        A = i
        break

for i in range(X):
    if 5 ** i > X:
        B = i
        break


for i in range(1, A):
    for j in range(1, B):
        if 3 ** i + 5 ** j == n:
            print(i, j)
            return

print(-1)
