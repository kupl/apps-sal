n = int(input())
d, x = map(int, input().split())
ans = 0
for i in range(n):
    a = int(input())
    if d % a == 0:
        ans += d // a
    else:
        ans += d // a + 1
print(ans + x)
