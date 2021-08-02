s = input()
t = input()
s = sorted(s)
t = sorted(t, reverse=True)
s_t = [s, t]
s_t.sort()
if s_t[0] == s and s_t[1] != s:
    print("Yes")
else:
    print("No")
