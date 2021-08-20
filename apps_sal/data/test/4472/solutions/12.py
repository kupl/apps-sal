from collections import Counter


def R():
    return map(int, input().split())


n = int(input())
s1 = input()
s2 = input()
ans = 0
for i in range(n // 2):
    t = [s1[i], s1[n - i - 1], s2[i], s2[n - i - 1]]
    c = sorted(list(Counter(t).values()))
    m = len(c)
    if m == 4:
        ans += 2
    elif m == 3:
        ans += 1
        if s1[i] == s1[n - i - 1]:
            ans += 1
    elif m == 2 and c[-1] == 3:
        ans += 1
if n % 2:
    p = (n - 1) // 2
    if s1[p] != s2[p]:
        ans += 1
print(ans)
