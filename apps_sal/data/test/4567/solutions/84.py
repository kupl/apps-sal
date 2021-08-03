n = int(input())
s = [int(input()) for _ in range(n)]
ans = 0
for i in range(n):
    for j in range(i, n):
        a = sum(s[:i]) + sum(s[j:])
        if a > ans and a % 10:
            ans = a
print(ans)
