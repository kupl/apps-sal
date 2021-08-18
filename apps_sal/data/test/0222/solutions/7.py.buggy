def check(t, s):
    cur_t = 0
    for j in range(len(s)):
        while cur_t < len(t) and t[cur_t] != s[j]:
            cur_t += 1
        if cur_t == len(t):
            return False
        cur_t += 1
    return True


s1 = input()
for i in range(45 * 1000, 0, -1):
    s2 = str(i * i)
    if check(s1, s2):
        print(len(s1) - len(s2))
        return
print(-1)
