n = int(input())
a = list(map(int, input().split()))
t = 0
ans = 0
for i in a + a:
    t = t + 1 if i else 0
    ans = max(ans, t)
print(ans)
