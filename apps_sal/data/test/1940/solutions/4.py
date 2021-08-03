n, k = map(int, input().split())
array = list(map(int, input().split()))
ans = 0
for i in range(n):
    ans += (array[i] + k - 1) // k
print((ans + 1) // 2)
