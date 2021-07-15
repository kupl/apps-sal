x, n = map(int, input().split())
ppp = []
if n != 0:
    ppp = list(map(int, input().split()))
ans = 0
for i in range(101):
    if x - i not in ppp:
        ans = x - i
        break
    if x + i not in ppp:
        ans = x + i
        break
print(ans)
