input()
s = list(input())
orig = len(s)

changed = True
while changed:
    changed = False
    for c in sorted(list(set(s)), reverse=True):
        for i in range(len(s)):
            if s[i] == c and ((i-1 >= 0 and ord(s[i-1]) == ord(s[i]) - 1) or 
                    (i + 1 < len(s) and ord(s[i+1]) == ord(s[i]) - 1)):
                s = s[:i] + s[i+1:]
                changed = True
                break
        if changed:
            break

print(orig - len(s))

