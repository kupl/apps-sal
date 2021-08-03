N, M = [int(_) for _ in input().split()]
l = 1
r = N
ans = []
for _ in range(M - M // 2):
    ans += [l, r]
    l += 1
    r -= 1
if (r - l) % 2 == (l + N - r) % 2:
    r -= 1
for _ in range(M // 2):
    ans += [l, r]
    l += 1
    r -= 1
ans = ans[:2 * M]
print(('\n'.join(f'{a} {b}' for a, b in zip(ans[::2], ans[1::2]))))
