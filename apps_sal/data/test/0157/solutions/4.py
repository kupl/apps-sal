a = int(input())
b = int(input())
c = int(input())
ans = 0
for x in range(a + 1):
    if x * 2 > b or x * 4 > c:
        continue
    ans = max(ans, x + 2 * x + 4 * x)
print(ans)
