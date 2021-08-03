def rle(s):
    tmp, count, ans = s[0], 1, []
    for i in range(1, len(s)):
        if tmp == s[i]:
            count += 1
        else:
            ans.append((tmp, count))
            tmp = s[i]
            count = 1
    ans.append((tmp, count))
    return ans


S = input()
ans = [str(0) for _ in range(len(S))]
Srle = rle(S)

itr = 0
for i in range(1, len(Srle), 2):
    itr += Srle[i - 1][1]
    Rtoeven = Srle[i - 1][1] // 2
    Ltoeven = Srle[i][1] // 2
    ans[itr - 1] = str((Srle[i - 1][1] - Rtoeven) + Ltoeven)
    ans[itr] = str(Rtoeven + (Srle[i][1] - Ltoeven))
    itr += Srle[i][1]
"""
Rtoeven は RLのRから偶数離れている個数
Ltoeven は RLのLから偶数離れている個数
"""
print(" ".join(ans))
