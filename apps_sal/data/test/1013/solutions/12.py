(n, m) = map(int, input().split())
ans = 4
if '1' in input():
    ans = 2
else:
    for i in range(n - 2):
        t = input()
        if '1' == t[0] or '1' == t[-1]:
            ans = 2
            break
if '1' in input():
    ans = 2
print(ans)
