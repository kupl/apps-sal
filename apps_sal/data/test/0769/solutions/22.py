a, b, c = list(map(int, input().split()))

used = set([a])
a *= 10
i = 1
while True:
    if a // b == c:
        print(i)
        return
    a %= b
    if a in used:
        break
    used |= set([a])
    a *= 10
    i += 1
print(-1)
