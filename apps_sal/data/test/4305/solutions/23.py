h, a = map(int, input().split())
if h % a == 0:
    ans = -1
else:
    ans = 0
while h >= 0:
    h -= a
    ans += 1
print(ans)
