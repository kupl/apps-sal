s = [max(0, len(x) - 1) for x in input().split('o')]
R = sum(s)
L = 0
ans = 0
for x in s:
    L += x
    R -= x
    ans += L * R
print(ans)
