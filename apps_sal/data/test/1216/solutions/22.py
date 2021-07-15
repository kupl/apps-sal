gl = ('a', 'e', 'i', 'o', 'u', 'y')

input()
s = input()

ans = []

i = 0
while i < len(s):
    if s[i] in gl:
        # print([j for j in s[i:] if j == s[i]])
        now = []
        for j in s[i:]:
            if j != s[i]:
                break
            now.append(j)

        i += len(now) - 1
        # print(now)
        ans.append(s[i])
        if len(now) == 2 and s[i] in ('o', 'e'):
            ans.append(s[i])

    else:
        ans += [s[i]]
    i += 1


print(*ans, sep='')

