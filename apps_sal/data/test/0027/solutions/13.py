n = int(input())
s = input()
ans = 1e18
for c in range(n // 2 + 1):
    curr = c + 1 + (n - 2 * c)
    if c == 0:
        curr -= 1
    s1 = s[:c] * 2
    b = True
    for i in range(len(s1)):
        if s1[i] != s[i]:
            b = False
            break
    #print(c, b, curr, s1)
    if b:
        ans = min(ans, curr)
print(ans)
