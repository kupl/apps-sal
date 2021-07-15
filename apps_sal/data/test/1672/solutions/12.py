n = int(input())
k = 0
ans = 0
for i in range(n):
    a = int(input())
    if k != a:
        ans += 1
        k = a
print(ans)
