n = int(input())
x = list(map(int, input().split()))
h = round(sum(x) / n)
ans = 0
for i in range(n):
    ans += (x[i] - h) ** 2
print(ans)
