a, b, c = map(int, input().split())
ans = c
if b < ans - 1:
    ans = b + 1
if a < ans - 2:
    ans = a + 2
print(3 * ans - 3)
