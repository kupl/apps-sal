s = [int(_) for _ in list(input())]
for i in range(len(s)):
    if 9-s[i] < s[i]:
        if (i == 0 and 9-s[i] == 0):
            continue
        s[i] = 9-s[i]
print(int(''.join([str(_) for _ in s])))

