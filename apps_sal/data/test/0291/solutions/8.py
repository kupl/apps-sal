(a, b) = map(int, input().split())
ans = 0
while a <= b:
    ans = ans + 1
    a = 3 * a
    b = 2 * b
print(ans)
