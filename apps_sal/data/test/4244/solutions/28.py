n = int(input())
x = list(map(int, input().split()))
ans = 1000000
for i in range(101):
    score = 0
    for j in range(n):
        score += (x[j] - i) ** 2
    ans = min(ans, score)
print(ans)
