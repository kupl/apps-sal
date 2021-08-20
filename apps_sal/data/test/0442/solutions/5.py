r = int(input())
ans = 'NO'
for i in range(1, 3 * int(r ** 0.5)):
    d = r - 1 - i - i ** 2
    if d < 1:
        break
    elif d % (i * 2) == 0:
        ans = (i, d // (i * 2))
        break
if ans == 'NO':
    print(ans)
else:
    print(*ans)
