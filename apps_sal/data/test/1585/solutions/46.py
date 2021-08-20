(x, y) = map(int, input().split())
(a, ans) = (x, 0)
while a <= y:
    a *= 2
    ans += 1
print(ans)
