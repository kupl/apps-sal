# n-1箇所に+をいれるかいれないかなのでbit全探索が可能
s = list(input())
ans = 0
for bit in range(1 << len(s) - 1):
    a = [int(s[0])]
    for i in range(len(s) - 1):
        if (bit >> i) & 1 == 1:
            a.append(int(s[i + 1]))
        else:
            a[-1] = 10 * a[-1] + int(s[i + 1])
    ans += sum(a)
print(ans)
