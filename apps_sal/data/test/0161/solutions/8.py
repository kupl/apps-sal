x = int(input())
(q1, ans) = (0, [])
while set(bin(x)[2:]) != {'1'}:
    if q1 % 2 == 0:
        t = bin(x)[2:]
        y = t.find('0')
        ans.append(len(t) - y)
        x ^= (1 << ans[-1]) - 1
    else:
        x += 1
    q1 += 1
print(q1)
if len(ans) > 0:
    print(*ans)
