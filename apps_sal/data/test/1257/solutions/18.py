
n, k = list(map(int, input().split()))

T = ["" for _ in range(n)]

t = 0
r = 0
for i in range(n):
    for j in range(k - 1):
        t += 1
        T[i] += str(t) + " "
for i in range(n):
    r += t + 1
    for j in range(k - 1, n):
        t += 1
        T[i] += str(t) + " "
print(r)
for i in range(n):
    print(T[i][:(len(T[i]) - 1)])
