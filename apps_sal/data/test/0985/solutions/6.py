n = int(input())

A = [0] * 3000
B = [0] * 3000

for i in range(n):
    x, y = list(map(int, input().split()))
    A[x + y] += 1
    B[x - y] += 1
ans = 0
for elem in A:
    ans += (elem * (elem - 1)) // 2
for elem in B:
    ans += (elem * (elem - 1)) // 2
print(ans)
