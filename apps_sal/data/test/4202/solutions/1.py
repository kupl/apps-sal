L, R = map(int, input().split())
kouho = set([])
while len(kouho) < 2019 and L <= R:
    temp = L % 2019
    kouho.add(temp)
    L += 1
A = list(kouho)
A.sort()
ans = 2018
for i in range(len(A)):
    for j in range(i + 1, len(A)):
        temp = A[i] * A[j] % 2019
        ans = min(ans, temp)
print(ans)
