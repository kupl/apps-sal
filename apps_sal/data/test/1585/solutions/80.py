(x, y) = map(int, input().split())
ans = 0
s = 0
c = 1
while s <= y:
    s = x * 2 ** c
    c += 1
    ans += 1
print(ans)
