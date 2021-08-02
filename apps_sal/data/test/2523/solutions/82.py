s = input()
n = len(s)
ans = n
s1 = s.count('1')
i = 0
while s1 != 0 and s1 != n:
    s1 -= int(s[i]) + int(s[i + n - 1])
    if n == 1:
        s1 += int(s[i])
    n -= 2
    ans -= 1
    i += 1
print(ans)
