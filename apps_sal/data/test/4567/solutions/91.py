n = int(input())
s = [int(input()) for _ in range(n)]

ss = sum(s)
ans = ss * min(1, ss % 10)

for i in range(n):
    score = ss - s[i]

    ans = max(ans, score * min(1, score % 10))

print(ans)
