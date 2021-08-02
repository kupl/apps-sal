n = int(input())
a = list(map(int, input().split()))
ans = 10e9
for i in range(n):
    k = 0
    for j in range(n):
        k += (abs(j - i) + j + i) * a[j] * 2
    ans = min(k, ans)
print(ans)
