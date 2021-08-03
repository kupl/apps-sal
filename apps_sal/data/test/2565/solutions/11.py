gans = []
for _ in range(int(input())):
    a0, a1, a2 = list(map(int, input().split()))
    b0, b1, b2 = list(map(int, input().split()))
    a0, b2 = a0 - min(a0, b2), b2 - min(a0, b2)
    a2, b2 = a2 - min(a2, b2), b2 - min(a2, b2)
    ans = -b2 * 2
    a1 -= b2
    b2 = 0
    ans += min(a2, b1) * 2
    a2, b1 = a2 - min(a2, b1), b1 - min(a2, b1)
    gans.append(ans)
print('\n'.join(map(str, gans)))
