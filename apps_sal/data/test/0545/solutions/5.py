import sys


n, t = [int(i) for i in input().split()]
s1 = input()
s2 = input()

common = 0
diff = 0
for i in range(n):
    if s1[i] == s2[i]:
        common += 1
    else:
        diff += 1

chars = 'abc'
ans = []
if common >= n - t:
    unc_common = n - t
    for i in range(n):
        if s1[i] == s2[i] and unc_common > 0:
            ans.append(s1[i])
            unc_common -= 1
        else:
            for char in chars:
                if char != s1[i] and char != s2[i]:
                    ans.append(char)
                    break
    print(''.join(ans))
else:
    unch = n - t - common
    unch1 = 0
    unch2 = 0
    if 2 * unch <= diff:
        for i in range(n):
            if s1[i] == s2[i]:
                ans.append(s1[i])
            else:
                if unch1 < unch:
                    ans.append(s1[i])
                    unch1 += 1
                elif unch2 < unch:
                    ans.append(s2[i])
                    unch2 += 1
                else:
                    for char in chars:
                        if char != s1[i] and char != s2[i]:
                            ans.append(char)
                            break
        print(''.join(ans))
    else:
        print(-1)
