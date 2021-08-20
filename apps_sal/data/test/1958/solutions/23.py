(n, p) = (int(_) for _ in input().split())
a = [input() for i in range(n)][::-1]
ans = 0
apple = 0
for s in a:
    apple *= 2
    if s == 'halfplus':
        apple += 1
    ans += p * apple // 2
print(ans)
