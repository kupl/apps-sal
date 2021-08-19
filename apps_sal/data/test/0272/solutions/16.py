s = input()
t = input()
letters = dict()
err = 0
ans = 0
answer = set()
for i in range(len(s)):
    if s[i] in letters and letters[s[i]] != t[i] or (t[i] in letters and letters[t[i]] != s[i]):
        print(-1)
        err = 1
        break
    elif not s[i] in letters:
        letters[s[i]] = t[i]
        letters[t[i]] = s[i]
        st = s[i] + ' ' + t[i]
        if s[i] == t[i]:
            continue
        answer.add(st)
        ans += 1
if err == 0:
    print(ans)
    for st in answer:
        print(st)
