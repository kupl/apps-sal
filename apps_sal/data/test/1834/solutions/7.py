n = int(input())
s = list(map(int, input().split()))
s.sort()
p = n // 2
ans = [0] * n
q = n
for i in range(1, n, 2):
    q -= 1
    ans[i] = s[q]
for i in range(0, n, 2):
    q -= 1
    ans[i] = s[q]
print(*ans)
