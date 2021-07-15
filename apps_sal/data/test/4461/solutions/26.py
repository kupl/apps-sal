h, w = list(map(int, input().split()))

if h % 3 == 0 or w % 3 == 0:
    print((0))
    return
ans = 10 ** 10
if h >= 3:
    ans = min(h, ans)

if w >= 3:

    ans = min(ans, w)
    # print(kouho)

for i in range(1, h):
    num1 = w * (i)
    num2 = (h - i) * (w // 2)
    num3 = (h - i) * (w - w // 2)
    kouho = [num1, num2, num3]
    kouho.sort()
    ans = min(ans, kouho[-1] - kouho[0])
for i in range(1, w):
    num1 = h * (i)
    num2 = (w - i) * (h // 2)
    num3 = (w - i) * (h - h // 2)
    kouho = [num1, num2, num3]
    kouho.sort()
    ans = min(ans, kouho[-1] - kouho[0])
print(ans)

