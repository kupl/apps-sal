n, k = map(int, input().split())
s = input()
k1 = k
k2 = k
a = b = ans = 0
for i in range(n):
    if s[i] == 'b': k1 -= 1
    else: k2 -= 1;
    while k1 < 0:
        if s[a] == 'b': k1 += 1
        a += 1
    while k2 < 0:
        if s[b] == 'a': k2 += 1
        b += 1
    ans = max(ans, i - a + 1, i - b + 1)
print(ans)
