s = str(input())
t = str(input())
ans = len(s) + len(t)
ind = -1
s_len = len(s)
t_len = len(t)
while abs(ind) <= s_len and abs(ind) <= t_len and (s[ind] == t[ind]):
    ans -= 2
    ind -= 1
print(ans)
