#abc076 C
from copy import deepcopy
s = list(input())
t = list(input())
ls = len(s)
lt = len(t)

rev_s = s[::-1]
rev_t = t[::-1]

for x in range(ls-lt+1):
    if rev_s[x:x+lt] == ["?"] * lt:
        for y in range(lt):
            rev_s[x+y] = rev_t[y]
        ns = rev_s[::-1]
        S = "".join(ns)
        ans = S.replace("?", "a")
        print(ans)
        return


for i in range(lt):
    for j in range(i, ls):
        if rev_t[i] == rev_s[j]:
            flag = True
            t_temp = deepcopy(rev_t)
            s_temp = deepcopy(rev_s)
            for k in range(-i, lt-i):
                if j+k >= ls or j+k < 0:
                    flag = False
                    break
                elif t_temp[i+k] == s_temp[j+k]:
                    pass
                elif s_temp[j+k] == "?":
                    s_temp[j+k] = t_temp[i+k]
                elif t_temp[i+k] != s_temp[j+k]:
                    flag = False
                    break
            if flag:
                ns = s_temp[::-1]
                S = "".join(ns)
                ans = S.replace("?", "a")
                print(ans)
                return

print("UNRESTORABLE")
