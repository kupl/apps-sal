(n, k) = map(int, input().split())
u = 0
arr = [0] * k
for i in range(n):
    a = int(input())
    arr[a - 1] += 1
for i in range(k):
    u += arr[i] // 2
print((n + 1) // 2 + u)
