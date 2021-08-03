n = int(input())
A = list(map(int, input().split()))
li = [0] * (n + 1)
for i in range(n - 1):
    b = A[i] - 1
    li[b] += 1
for i in range(n):
    print(li[i])
