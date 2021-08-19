s = input()
t = input()
s_streak = 0
s_streak_ind = -1
for j in range(len(s) - 1, -1, -1):
    for i in range(j, -1, -1):
        if s_streak_ind == -1:
            if s[i] == '?' or s[i] == t[len(t) - 1 - s_streak]:
                if s_streak == len(t) - 1:
                    s_streak_ind = i
                    s_streak = 0
                else:
                    s_streak += 1
            else:
                s_streak = 0
    s_streak = 0
if s_streak_ind == -1:
    print('UNRESTORABLE')
else:
    ansl = []
    for i in range(len(s)):
        if s[i] == '?':
            if s_streak_ind <= i < s_streak_ind + len(t):
                ansl.append(t[i - s_streak_ind])
            else:
                ansl.append('a')
        else:
            ansl.append(s[i])
    print(''.join(ansl))
