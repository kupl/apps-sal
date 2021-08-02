a = int(input())
b = list(map(int, input().split()))
c = 0
ans = 0
for i in range(a):
    if b[i] >= c:
        ans += 1
    c = max(c, b[i])
print(ans)
