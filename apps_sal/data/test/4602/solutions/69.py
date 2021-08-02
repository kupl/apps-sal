n = int(input())
k = int(input())
x = list(map(int, input().split()))

ans = 0
for i in range(n):
    ans += min(abs(x[i] - 0), abs(x[i] - k))
print(ans * 2)
