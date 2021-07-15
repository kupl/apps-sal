n = int(input())

total = int(n * (n + 1) / 2)

l = []
cur = 0
if total % 2 == 0:
    print(0)
    target = total // 2
    while cur != target:
        if target - cur <= n:
            l.append(target - cur)
            break
        else:
            l.append(n)
            cur += n
            n -= 1
else:
    print(1)
    target = total // 2
    while cur != target:
        if target - cur <= n:
            l.append(target - cur)
            break
        else:
            l.append(n)
            cur += n
            n -= 1
print(len(l), end = ' ')
print(*l)
