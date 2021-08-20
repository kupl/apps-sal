n = int(input())
arr = list(map(int, input().split()))
m = int(1000000000000.0)
ans = 1
for i in range(n):
    k = arr[i] // n
    k *= n
    while k + i < arr[i]:
        k += n
    if k < m:
        m = min(m, k)
        ans = i
print(ans + 1)
