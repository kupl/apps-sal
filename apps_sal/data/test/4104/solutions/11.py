s = input()
val = eval(s)
for i in range(len(s)):
    if s[i] ==  '+':
        j = i + 1
        c = -5
        while j < len(s) and s[j] != '+' and s[j] != '-':
            c *= 10
            j += 1
        val += c
    elif s[i] == '-':
        j = i + 1
        c = 3
        while j < len(s) and s[j] != '+' and s[j] != '-':
            c *= 10
            j += 1
        val += c
print(val)
