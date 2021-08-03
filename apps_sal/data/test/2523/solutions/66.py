S = input()
l = len(S)
if l % 2 == 1:
    m = S[l // 2]
    c = 1
    for i in range(l // 2):
        if S[l // 2 - i - 1] == m and S[l // 2 + i + 1] == m:
            c += 2
        else:
            break
    ans = c + (l - c) // 2
else:
    m1 = S[l // 2 - 1]
    m2 = S[l // 2]
    c = 0
    if m1 == m2:
        c = 2
        for i in range(l // 2 - 1):
            if S[l // 2 - i - 2] == m1 and S[l // 2 + i + 1] == m1:
                c += 2
            else:
                break
    ans = c + (l - c) // 2
print(ans)
