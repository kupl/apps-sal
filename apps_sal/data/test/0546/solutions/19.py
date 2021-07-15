import re
abc = set(list('abcdefghijklmnopqrstuvwxyz'))

good = set(input())
sp = {'?', '*'}

bad = abc - good
ans = []

pat = input()
pl = len(pat)
for _ in range(int(input())):
    hasstar = False
    answered = False
    q = input()
    d = len(q) - pl
    if d < -1 or (d == -1 and "*" not in pat):
        ans.append("NO")
        continue
    else:
        i = 0
        j = 0
        while i < pl:
            if (pat[i] == '?' and q[j] in bad) or (pat[i] not in sp and q[j] != pat[i]):
                ans.append("NO")
                answered = True
                break
            elif pat[i] == '*':
                hasstar = True
                if any(q[k] in good for k in range(j, j+d+1)):
                    ans.append("NO")
                    answered = True
                    break
                j += d
            i += 1
            j += 1
        if not answered:
            if not hasstar:
                if pl == len(q):
                    ans.append('YES')
                    answered = True
                else:
                    ans.append('NO')
                    answered = True
            else:
                ans.append("YES")
                answered = True
print('\n'.join(ans))

