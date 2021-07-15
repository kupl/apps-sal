n, s = input().split()
ans = 0
for j in range(int(n)):
    c1, c2 = 0, 0
    for i in range(j, int(n)):
        if s[i] == 'T': c1 += 1
        elif s[i] == 'A': c1 -= 1
        elif s[i] == 'C': c2 += 1
        else: c2 -= 1
        if c1 == 0 and c2 == 0: ans += 1
print(ans)
