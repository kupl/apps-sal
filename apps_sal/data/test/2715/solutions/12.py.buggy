k = int(input())
n = 50

q, r = divmod(k, n)
A = [n - 1] * n
for i in range(n):
    A[i] += q

for i in range(r):
    A[i] += n + 1
    for j in range(n):
        A[j] -= 1

print(n)
print((*A))
