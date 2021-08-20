def f(n):
    return n * (n + 1) // 2


(a, m) = map(int, input().split())
s = list(input())
t = set(input().split())
p = 0
i = 0
ans = 0
while p < len(s):
    if s[p] not in t:
        ans += f(i)
        i = 0
    else:
        i += 1
    p += 1
ans += f(i)
print(ans)
