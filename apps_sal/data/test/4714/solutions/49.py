(a, b) = map(int, input().split())
ans = 0
for i in range(a, b + 1):
    i = str(i)
    if i == i[::-1]:
        ans += 1
print(ans)
