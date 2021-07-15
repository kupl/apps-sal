x, p = map(int, input().split())

ans = float('inf')
for i in range(0, 100001):
    y = x - i * p
    if (y <= 0):
        continue
    aaa = 0
    for j, el in enumerate(reversed(bin(y))):
        if (el == '1'):
            aaa += 2**j
            if (aaa >= i):
                break
    bbb = bin(y).count('1')
    if (bbb <= i <= aaa):
        ans = min(ans, i)

if ans == float('inf'):
    ans = -1

print(ans)
