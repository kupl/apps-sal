n, h = map(int, input().split())
alst = []
blst = []
for _ in range(n):
    a, b = map(int, input().split())
    alst.append(a)
    blst.append(b)
blst.sort(reverse = True)
a = max(alst)
ans = 0
for num in blst:
    if num < a:
        ans += (h - 1) // a + 1
        break
    else:
        ans += 1
        h -= num
        if h <= 0:
            break

else:
    ans += (h - 1) // a + 1
print(ans)
