s = input()
ans = 0
for bit in range(1 << len(s) - 1):
    f = s[0]
    for i in range(len(s) - 1):
        if bit & 1 << i:
            f += '+'
        f += s[i + 1]
    ans += sum(map(int, f.split('+')))
print(ans)
