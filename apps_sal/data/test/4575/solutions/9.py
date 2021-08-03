n = int(input())
d, x = map(int, input().split())
ans = 0
for i in range(n):
    a = int(input())
    b = d // a
    c = d % a
    if c != 0:
        ans += b + 1
    else:
        ans += b
print(ans + x)
