s, p = map(int, input().split())
for n in range(1, p + 1):
    if n * n > p: break
    if p % n == 0 and n + p // n == s:
        print('Yes')
        return

print('No')
