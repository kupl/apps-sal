def read(): return list(map(int, input().split()))


n = int(input())
a = sorted(read())
T = int(input())
ans = 0
j = 0
for i in range(n):
    while j < n and a[j] - a[i] <= T:
        j += 1
    ans = max(ans, j - i)
print(ans)
