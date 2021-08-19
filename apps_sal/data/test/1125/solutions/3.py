def main(n, a):
    s = a[0] + a[1]
    z = 0
    for ai in a[2:]:
        z ^= ai
    if s - z < 0 or (s - z) % 2 == 1:
        return -1
    d = (s - z) // 2
    if d & z != 0:
        return -1
    if not d <= a[0]:
        return -1
    part = []
    i = 0
    while z // pow(2, i):
        if z // pow(2, i) % 2 == 1:
            part.append(pow(2, i))
        i += 1
    ans = float('inf')
    k = len(part)
    x = 0
    while part:
        tmp = part.pop()
        if d ^ x + tmp <= a[0]:
            x += tmp
    return a[0] - (d ^ x) if d ^ x else -1


n = int(input())
a = list(map(int, input().split()))
print(main(n, a))
