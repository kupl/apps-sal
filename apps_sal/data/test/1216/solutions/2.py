vowel = {'a', 'e', 'i', 'o', 'u', 'y'}

n = int(input())
s = input()

l = len(s)

ans, last_c, i = "", ' ', 0
for c in s:
    if not c in vowel:
        ans += c
    else:
        if c != last_c:
            ans += c
        else:
            if c == 'e' or c == 'o':
                if (i + 1 >= l or s[i + 1] != c) and (i < 2 or s[i - 2] != c):
                    ans += c

    last_c = c

    i += 1

print(ans)
